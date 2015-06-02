#!/usr/bin/python

#############################################
# TODO: add error detection and error messages
# TODO: add better perfect rhyme detection <-- DONE???
# TODO: add scoring
# TODO: add support for more than 1 text file
# TODO: add detection of more rhymes <-- DONE
# TODO: lots of other shit basically <-- Well... yeah
# TODO: separate methods from testing <-- what's dat mean <- I'll take care of this
# TODO: change methods to use already transcribed strings (you know, speed probably)
# TODO: multi syllabic rhymes <-- DONE
# TODO: scrape AZ Lyrics and scrub <-- basics are done
# TODO: denstiy plot of rhymes
# TODO: pick out a nonwestern for us to take spring semester
# TODO: nice todo, also scrub rhymes for punctuation because CMU dict is fucking stupid <-- DONE
# TODO: measure *based on syllables* <-- whats dat mean <- nvm
#############################################

#############################################
# NEW TODOS
# TODO: handle words not in cmudict <- this is hard
# TODO: make big wrap method that does all rhyme detection
# TODO: error handling with web scraping (ie no results or first result is not right one)
# TODO: put scraping and processing together
# TODO: find_matching_phonemes needs some love or to be deleted
#############################################

import sys
import nltk
import pprint
from nltk.corpus import cmudict
from collections import defaultdict, OrderedDict

#########################################
# BEGIN: Functions that act like macros #
#########################################

def line_break():
    print("\n")

def horiz_line():
    print("==============================")

#######################################
# END: Functions that act like macros #
#######################################

transcr = cmudict.dict()

vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']

# read_and_scrub_text_file(i)
# Description: reads the text file and returns a scrubbed list of strings ready to transcribe
# param      : i, an integer (>= 1) referring to which argument to open and read
# return     : a list of scrubbed strings

def read_and_scrub_text_file(i):
    file_1 = open(sys.argv[1])        # Open text file at first argument of command line in *read* mode
    file1_lines = file_1.readlines()  # returns list of strings with new line characters at the end
    lines_scrubbed = []               # initialize empty list for return value

    for s in file1_lines:             # loop through each line read in from the text file
        lines_scrubbed.append(s[:-1]) # purge the new line characters so now we have a clean list of strings to transcribe
    file_1.close()                    # close the file to free up resources

    return lines_scrubbed

# scrub_punct(lines)
# Description: takes a line and scrubs it of all punctuation
# param      : a string
# return     : a punctuation scrubbed string (oooo, ahhhhh)

def scrub_punct(lines):
    line = lines.split()                        # list of words in line
    temp_line = []                              # scrubbed line
    for j in line:                              # go word by word
        if j.isalpha():                         # no punctuation to remove in this word in the line
            temp_line.append(j)                 # add normaly
        else:                                   # there is punctuation to remove
            temp_word = []
            for k in j:                         # go letter by letter
                if k.isalpha() or k == "'":     # this is not a punctuation character
                    temp_word.append(k)         # add to the currnet scrubbed word
            temp_line.append("".join(temp_word))
    return (" ".join(temp_line))                # add to list of scrubbed lines

# transcribe_string(string)
# Description: transcribes a string into its phonemes and prints the result out.
# param      : string str to transcribe
# return     : list of lists of phonemes

def transcribe_string(string):
    results = [transcr[w][0] for w in string.lower().split()]  # transcribes the sample string given to the CMU Dictionary.

    return results

# transcribe_list(l)
# Description: converts a list of strings into a list of list of lists of phonemes per word
# param      : list of strings
# return     : transcribed list of list of lists of phonemes

def transcribe_list(l):
    list_transcription = []                             # initialize return value to empty list
    for w in l:                                         # iterate through each string in argument
        list_transcription.append(transcribe_string(w)) # transcribe string and append list of phonemes to return value

    return list_transcription

# detect_perfect_rhyme_two_lines(a, b)
# Description: detects a perfect rhyme (definition below) between 2 passed strings
#            : perfect rhyme: a rhyme in which the endings of words sound exactly the same
#            : http://genius.com/posts/24-Rap-genius-university-rhyme-types
# param      : *un-transcribed* string 1, *un-transcribed* string 2
# return     : True if perfect rhyme detected, False if not

def detect_perfect_rhyme_two_lines(a, b):
    a_syl = syllable_string(a) # Transcribe string a into its syllables
    b_syl = syllable_string(b) # Transcribe string b into its syllables 

    print a_syl
    print b_syl

    a_last = a_syl[-1][0]                                               # get last word of each line
    b_last = b_syl[-1][0]

    print a_last
    print b_last

    a_index = len(a_last)-1                                             # index of last phoneme
    b_index = len(b_last)-1
    while min(a_index, b_index) >= 0:                                   # while the smaller index is greater than 0
        if a_last[a_index] != b_last[b_index]:                          # if phonemes don't match, not a perfect rhyme
            break
        if is_vowel(a_last[a_index]) and a_index < len(a_last):         # if we hit a vowel and this vowel is not the last phoneme in the word    
            return True                                                 # ^ this prevents words like gamma and camera from being considered perfect rhyme
        a_index-=1
        b_index-=1
    return False

# detect_alliteration(a)
# Description: detects alliterations within ONE line
# param      : *un-transcribed* string a
# return     : a list of tuples, first element is phoneme, second is the number of times it appears, third is index in line where assonance begins
#            : lenght of this list gives you total number of alliterations in line

def detect_alliteration(a):
    a_transcr = transcribe_string(a)                           # Transcribe string a into its pronunciations
    ret = []
    x = 0                                                      # go through words
    while x < len(a_transcr):
        num_times = 0
        y = 1
        stop = False
        while not(stop) and y < (len(a_transcr) - x):
            stop = True
            if a_transcr[x][0] == a_transcr[x + y][0]:
                num_times += 1
                stop = False                                   # keep searching forwards
                y += 1                                         # look one word further
                                                               # figure out how to check 1-2 more words in advnace
        if num_times > 0:
            ret.append((a_transcr[x][0], num_times, x))        # add this alliteration to the list
            x = x + y + 1                                      # start searching for more alliterations after this one ends to avoid double counting
        else:
            x += 1
    return ret

# detect_assonance_in_line(a)
# Description: detects assonance within ONE line
# param      : *un-transcribed* string a
# return     : a list of tuples, first element is phoneme, second is the number of times it appears, third is index in line where assonance begins
#            : lenght of this list gives you total number of assonance in line

def detect_assonance_in_line(a):
    a_transcr = transcribe_string(a)                 # Transcribe string a into its pronunciations
    ret = []
    x = 0                                            # go through words
    while x < len(a_transcr):
        vowels = []
        newX = x + 1
        for z in a_transcr[x]:                       # find the vowels in the word
            if is_vowel(z):
                vowels.append(z)
        for w in vowels:                             # check each vowel to see if there is assonance within the line
            num_times = 0
            y = 1
            stop = False
            while not(stop) and y < (len(a_transcr) - x):
                stop = True
                if w in a_transcr[x + y]:
                    num_times += 1
                    stop = False                     # keep searching forwards
                    y += 1                           # look one word further
                                                     # figure out how to check 1-2 more words in advnace
            if num_times > 0:
                ret.append((w, num_times, x))        # add this assonance to the list
                if x + y + 1 > newX:
                    newX = x + y + 1                 # start searching for more assonance after this one ends to avoid double counting
        x = newX
    return ret

# is_vowel(phoneme)
# Description: determines if a phoneme is a vowel sound
# param      : phoneme string
# return     : true if phoneme is a vowel sound, else false

def is_vowel(phoneme):
    if phoneme[-1].isdigit:
        phoneme = phoneme[:-1]
    if phoneme in vowels:
        return True
    else:
        return False

# syllable_count(word)
# Description: counts the number of syllables in a transcribed word
#            : this only works for a single word, not a line
# param      : list of phonemes (a transcribed string word)
# return     : integer number of syllables

def syllable_count(phonemes):
    ret = 0
    for x in phonemes:
        for y in x:
            if y[-1].isdigit():         # if the phoneme ends in a number, marks a syllable
                ret+=1
    return ret

# syllable_word(phonemes)
# Description: returns a list with each element representing the phonemes that make up a syllable in that word
# param      : list of phonemes (a transcribed string word)
# return     : list of lists of phonemes; each element of the main list constitutes a syllable

def syllable_word(phonemes):
    ret = []
    count = 1
    for x in phonemes:                                                # iterate through phonemes for that word
        temp = []
        for y in x: 
            temp.append(y) 
            if y[-1].isdigit():                                       # if the phoneme ends in a digit, then we know it's the end of that syllable 
                ret.append(temp)
                temp = []
        if (len(phonemes) == count) and not(len(temp) == 0):          # tack on last few phonemes if there are any left
            ret[-1] += temp
        count += 1
    return ret

# syllable_string(l)
# Description: we want a list of syllables for the string you enter
# param      : string, not already transcribed
# return     : list of list of syllables by word

def syllable_string(s):
    ret = []
    l = s.split(' ')

    for w in l:                                        # for every word in the list
       ret.append(syllable_word(transcribe_string(w))) # syllable-ize that word

    return ret

# syllable_string_no_word_boundaries(s)
# Description: we want a list of syllables for the string you enter, without word divisions
# param      : string, not already transcribed
# return     : list of syllables
#            : I now realize how stupid this method was

def syllable_string_no_word_boundaries(s):
    ret = []
    l = s.split(' ') # split s into constituent words

    for w in l: # for every word in the list
        werd = syllable_word(transcribe_string(w))
        for syl in werd:
            ret += syl

    return ret

# syllable_total(l)
# Description: Stupid Method
# param      : *not already trancribed* list of strings
# return     : big list of syllables per line (NOT BY WORD, as in: unseparated)

def syllable_total(l):
    ret = []
    for s in l:
        syl_str = syllable_string(s)
        temp = []
        for line in syl_str:
            temp += line 
        ret.append(temp)

    return ret

# find_matching_phonemes(a, b)
# Description: finds matching phonemes between a, b, and returns a list of booleans corresponding with indices and whether they match
#            : this is going to be really hacky
# param      : list of phonemes a, list of phonemes b
# return     : list of booleans

def find_matching_phonemes(a, b):
    # maybe i will fix this method later
    return

# phoneme_freq(l)
# Description: creates a frequency dict of phonemes in a line and sorts by frequency of appearance
# param      : transcribed line to scanalyze (I am a born rapper)
# return     : sorted frequency dict by number of phonemes (type OrderedDict)
# note       : in hindsight this might be totally unnecessary <-- i dont think it is since your vowel freq and allit freq do this for the phonemes we care about

def phoneme_freq(l):
    d = defaultdict(int)                                      # default dict with value int

    for w in l:                                               # for every word in the list
        for p in w:                                           # and every phoneme in the word
            d[p] += 1                                         # add it/increment it in the dict

    od = OrderedDict(sorted(d.items(), key = lambda t: t[1])) # then add it to an OrderedDict sorted by value
    
    return od

# vowel_freq(l), originally named ass_freq(l) <-- haha, not everything has to do with your ass johnny
# Description: shows the most frequent vowels in that line
# param      : transcribed list of phonemes (only one string)
# return     : OrderedDict of vowel phonemes to their frequency of appearance

def vowel_freq(l):
    d = defaultdict(int)                                                      # create defaultdict

    for w in l:                                                               # for every word in the list of lists of phonemes
        for p in w:                                                           # for every list of phonemes
            if is_vowel(p):                                                   # if that is a vowel
                d[p] += 1                                                     # increment its count in the dictionary

    od = OrderedDict(sorted(d.items(), key = lambda t: t[1], reverse = True)) # add these in descending order to the OrderedDict

    return od

# allit_freq(l)
# Description: Which alliterations are most frequent?
# param      : transcribed list of phonemes (only one string)
# return     : OrderedDict of alliteration phonemes to their frequency of appearance in *descending order*

def allit_freq(l):
    d = defaultdict(int)                                                      # create defaultdict

    for w in l:                                                               # for every list in the list of phonemes
        d[w[0]] += 1                                                          # add its first sound to the default dictionary

    od = OrderedDict(sorted(d.items(), key = lambda t: t[1], reverse = True)) # add these in descending order to the OrderedDict

    return od

# extract_vowels(l)
# Description: extracts vowels from a list of phonemes
# param      : list of phonemes to extract vowels from 
# return     :  sequence of vowels from the passed in list of phonemes

def extract_vowels(l):
    ret = []

    for x in l        :   # for every phoneme in the list
        if is_vowel(x):   # if it belongs to the list of vowels
            ret.append(x) # add that to the return list
    return ret

def extract_vowels_from_string(l):
    """
    Extracts vowels from an untranscribed string.
        param: untranscribed string
        return: list of vowels inside untranscribed string
    """
    ret = []
    transcr_lst = transcribe_string(l)

    for s in transcr_lst:
        vowels = extract_vowels(s)
        for v in vowels:
            ret.append(v)

    return ret
    

# multi_sequence(a, b)
# Description: What is the longest ending multisyllabic rhyme between 2 lines?
# param      : untranscribed string a, b
# return     : longest matching sequence between the two

def multi_sequence(a, b):
    syll_a = syllable_string_no_word_boundaries(a) # i realized how stupid this was after i wrote it... don't comment :)
    syll_b = syllable_string_no_word_boundaries(b)

    vowels_a = extract_vowels(syll_a)
    vowels_b = extract_vowels(syll_b)

    sequence = []

    for i in range(-1, -1 * min(len(a), len(b)), -1): # loop from the end of each array in steps of -1 <- very clever <- xie xie
        if vowels_a[i] == vowels_b[i]:
            sequence.insert(0, vowels_a[i])
        else:
            break

    return sequence
