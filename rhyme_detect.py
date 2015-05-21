#!/usr/bin/python

#############################################
# TODO: add error detection and error messages
# TODO: add better perfect rhyme detection
# TODO: add scoring
# TODO: add support for more than 1 text file
# TODO: add detection of more rhymes
# TODO: lots of other shit basically
# TODO: separate methods from testing
# TODO: change methods to use already transcribed strings (you know, speed probably)
########################## big one
# TODO: measure *based on syllables*
#############################################

import sys
import nltk
from nltk.corpus import cmudict

###########################
# BEGIN: GLOBAL VARIABLES #
###########################

# Sample rhymes in the form of a string, or a list of strings
# More sample rhymes are located in the text files
# Import text files by using command line arguments

# Lose Yourself - Eminem
LOSE_YOURSLEF = ["His palms are sweaty, knees weak, arms are heavy",
                 "There's vomit on his sweater already, mom's spaghetti",
                 "He's nervous, but on the surface he looks calm and ready to drop bombs",
                 "But he keeps on forgetting what he wrote down",
                 "The whole crowd goes so loud",
                 "He opens his mouth, but the words won't come out"]

PERFECT_RHYME = ["This is a perfect rhyme", 
                 "bitches split on a dime"]

SAMPLE_TEXT = "Mackerel bat from hell"

SAMPLE_TEXT2 = "Wow Jay C is asking for it, gonna punch him in a little bit" # that doesn't rhyme, fish can't rap, happy?

transcr = cmudict.dict()

#########################
# END: GLOBAL VARIABLES #
#########################

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
    a_transcr = transcribe_string(a) # Transcribe string a into its pronunciations
    b_transcr = transcribe_string(b) # Transcribe string b into its pronunciations

    if a[-1] == b[-1]: # if the items at the last indices match, return True
        return True
    return False       # else, return False

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

    for x in phonemes:          # iterate through phonemes for that word
        temp = []
        for y in x:
            temp.append(y)
            if y[-1].isdigit(): # if the phoneme ends in a digit, then we know it's the end of that syllable 
                ret.append(temp)
                temp = []
    ret.append(temp)            # don't forget the ending syllable 

    return ret

# syllables_list(l)
# Description: we want a 
def syllables_list(l):
    ret = []

    for w in l:                     # for every word in the list
       ret.append(syllable_word(w)) # syllable-ize that word

    return ret

# find_matching_phonemes(a, b)
# Description: finds matching phonemes between a, b, and returns a list of booleans corresponding with indices and whether they match
#            : this is going to be really hacky
# param      : list of phonemes a, list of phonemes b
# return     : list of booleans

# i'm too tired for comments right now check the google doc i left an explanation therrre
def find_matching_phonemes(a, b):
    syllables_a = syllables_list(a)
    syllables_b = syllables_list(b)
    
    print("DO THEY HAVE THE SAME NUM OF SYLLALBES?")
    print(len(syllables_a))
    print(len(syllables_b))

    return

#    comb = [a, b]
#    tot = [[],[]]
#    ret = []
#
#    min_length = 999999
#    counter = 0
#
#    for i in range(len(comb)):
#        for s in comb[i]:
#            for x in s:
#                counter += 1
#                tot[i].append(x)
#        
#        if (counter < min_length):
#            min_length = counter
#        counter = 0
#
#    for i in range(min_length - 1):
#        if tot[0][i] == tot[1][i]:
#            ret.append(True)
#        else:
#            ret.append(False)
#
#    return ret


#######################
# BEGIN: TEST SECTION #
#######################

#########################
# BEGIN SCRUB TESTS #
#########################

horiz_line()
print("BEGIN TESTS")
horiz_line()

if (len(sys.argv) > 1):
    line_break()
    print("ARGUMENTS DETECTED")
    print("TEST COMMAND LINE:")
    print("Argument List " + str(sys.argv))
    print("Number of arguments: " + str(len(sys.argv)))
    print("SCRUBBED LINES:")
    print(read_and_scrub_text_file(1))

line_break()
print("TESTING: transcribe_string(SAMPLE_TEXT)")
sample_transcr = transcribe_string(SAMPLE_TEXT) # test that transcribe_string function works
print(sample_transcr)                           # Prints out phonemes for "Mackerel bat from hell"

line_break()
print("TESTING: transcribe_list(PERFECT_RHYME)")
perfect_transcr = transcribe_list(PERFECT_RHYME) # test that transcribe_list function works correctly
print(perfect_transcr)                           # output should match what we have below
print("WHAT ARE THE LENGTHS OF EACH TRANSCRIPTION")
arr = [0,0]
for i in range(len(perfect_transcr)):
    for t in perfect_transcr[i]:
        for s in t:
            arr[i] += 1
print(arr)


line_break()
print("TEST FOR MATCH: transcribe_list(PERFECT_RHYME)") # test for matching output
for s in PERFECT_RHYME:
    print(transcribe_string(s))                         # transcribe_list ouputs match! yay!

########################
# END SCRUB TESTS #
########################

#########################
# BEGIN DETECTION TESTS #
#########################

line_break()
horiz_line()
print("Now comes the detection output:")
horiz_line()

line_break()
print("TEST FOR PERFECT RHYME:")                                          # test that perfect rhyme detection works
print(PERFECT_RHYME)                                                      # ['This is a perfect rhyme', 'bitches split on a dime']
print(detect_perfect_rhyme_two_lines(PERFECT_RHYME[0], PERFECT_RHYME[1])) # Expected: True (yay!)

line_break()
print("TEST FOR MATCHING PHONEMES:")
print(find_matching_phonemes(transcribe_string(PERFECT_RHYME[0]), transcribe_string(PERFECT_RHYME[1])))

########################
# END DETECTION TESTS #
########################

#########################
# BEGIN SYLLABLE TESTS #
#########################

line_break()
horiz_line()
print("Jay C in the hiz-house testing dem syllables:")
horiz_line()

line_break()
print("TEST FOR SINGLE WORD:") # next test: mack-er-el
print("AMAZING")
print(syllable_count(transcribe_string("amazing")))
print(syllable_word(transcribe_string("amazing")))
print(transcribe_string("amazing"))

########################
# END SYLLABLE TESTS #
########################

#####################
# END TEST SECTION #
#####################