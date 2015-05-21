#!/usr/bin/python

import nltk
from nltk.corpus import cmudict

# Sample rhymes as a string, or a list of strings
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

SAMPLE_TEXT2 = "Wowwwww Jay C is asking for it"

transcr = cmudict.dict()

## Description: transcribes a string into its phonemes and prints the result out.
# param: string str to transcribe
# return: list of lists of phonemes

def transcribe_string(string):
    results = [transcr[w][0] for w in string.lower().split()]  # transcribes the sample string given to the CMU Dictionary.

    return results

print(transcribe_string(SAMPLE_TEXT)) # Prints out phonemes for "Mackerel bat from hell"

for s in PERFECT_RHYME:
    print(transcribe_string(s))

