#!/usr/bin/python

import sys
import nltk
from nltk.corpus import cmudict

# Sample rhymes as a string, or a list of strings
# More sample rhymes are located in the text files.
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

SAMPLE_TEXT2 = "Wowwwww Jay C is asking for it" # that doesn't rhyme, fish can't rap

transcr = cmudict.dict()

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

if (len(sys.argv) > 1):
    horiz_line()
    print("TEST COMMAND LINE:")
    print("Argument List " + str(sys.argv))
    print("Number of arguments: " + str(len(sys.argv)))
    print("SCRUBBED LINES:")
    print(read_and_scrub_text_file(1))

horiz_line()
print("TESTING: transcribe_string(SAMPLE_TEXT)")
sample_transcr = transcribe_string(SAMPLE_TEXT) # test that transcribe_string function works
print(sample_transcr)                           # Prints out phonemes for "Mackerel bat from hell"

horiz_line()
print("TESTING: transcribe_list(PERFECT_RHYME)")
perfect_transcr = transcribe_list(PERFECT_RHYME) # test that transcribe_list function works correctly
print(perfect_transcr)                           # output should match what we have below

horiz_line()
print("TEST FOR MATCH: transcribe_list(PERFECT_RHYME)") # test for matching output
for s in PERFECT_RHYME:
    print(transcribe_string(s))                         # transcribe_list ouputs match! yay!

horiz_line()
print("Now comes the detection output:")

print("TEST FOR PERFECT RHYME:")                                          # test that perfect rhyme detection works
print(PERFECT_RHYME)                                                      # ['This is a perfect rhyme', 'bitches split on a dime']
print(detect_perfect_rhyme_two_lines(PERFECT_RHYME[0], PERFECT_RHYME[1])) # Expected: True (yay!)

