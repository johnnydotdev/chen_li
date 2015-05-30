#!/usr/bin/python

from detection.rhyme_detect import *
from detection.scrub import *

###########################
# BEGIN: GLOBAL VARIABLES #
###########################

# Sample rhymes in the form of a string, or a list of strings
# More sample rhymes are located in the text files
# Import text files by using command line arguments

# Lose Yourself - Eminem
LOSE_YOURSELF = ["His palms are sweaty knees weak arms are heavy",
                 "There vomit on his sweater already moms spaghetti",
                 "He nervous but on the surface he looks calm and ready to drop bombs",
                 "But he keeps on forgetting what he wrote down",
                 "The whole crowd goes so loud",
                 "He opens his mouth but the words wont come out"]

PERFECT_RHYME = ["This is a perfect rhyme", 
                 "bitches split on a dime"]

BREAK_PERFECT_RHYME = ["This is NOT a perfect rhyme and with some luck",
                       "The method will know this and not be a dick"]

BREAK_PERFECT_RHYME_YET_AGAIN = ["Nice try Johnny boy your effort was good",
                                "but I have a leg up or at least a foot"]

ALLITERATION_RHYME1 = ["Look I was gonna go easy on you and not to hurt your feelings",
                      "But I'm only going to get this one chance"]

ALLITERATION_RHYME2 = ["Big big booty what you got a big booty"]

ASSONANCE_RHYME = ["Maybe bake cake Jay C rapper star"]

SAMPLE_TEXT = "Mackerel bat from hell"

SAMPLE_TEXT2 = "Wow Jay C is asking for it, gonna punch him in a little bit" # that doesn't rhyme, fish can't rap <<< happy? <- :(

RAP_GOD = ["I'm beginning to feel like a Rap God, Rap God",
           "All my people from the front to the back nod, back nod"]

HOL_UP = ["I wrote this record while thirty thousand feet in the air",
          "Stewardess complimenting me on my happy hair",
          "If I can fuck her in front of all of these passengers",
          "They'll probably think I'm a terrorist eat my asparagus",
          "Then I'm asking her thoughts of a young bigger fast money and freedom",
          "A crash dummy for dollars I know you dying to meet them",
          "I'll holly die in a minute just bury me",
          "With twenty bitches twenty million and a Cop town fitted"]

GET_RID_OF_DAT_PUNCT = "This'll, have: a; (ton) of _pointless -punctuation"

#########################
# END: GLOBAL VARIABLES #
#########################

#####################
# BEGIN SCRUB TESTS #
#####################

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

line_break()
print("TEST FOR PUNCTUATION SCRUBBING:")
print GET_RID_OF_DAT_PUNCT
print scrub_punct(GET_RID_OF_DAT_PUNCT)

line_break()
print("TEST FOR SCRUB.PY")
scrub_lyrics("rap_god.txt")

###################
# END SCRUB TESTS #
###################

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
print(transcribe_list(PERFECT_RHYME))
print(detect_perfect_rhyme_two_lines(PERFECT_RHYME[0], PERFECT_RHYME[1])) # Expected: True (yay!)

line_break()
print("TEST FOR PERFECT RHYME:")                                            # test that perfect rhyme doesnt give false positives
print(BREAK_PERFECT_RHYME)                                                  # 'This is NOT a perfect rhyme and with some luck', 'The method will know this and not be a dick']
print(detect_perfect_rhyme_two_lines(BREAK_PERFECT_RHYME[0], BREAK_PERFECT_RHYME[1])) # Expected: False (boo! :( )

line_break()
print("TEST FOR PERFECT RHYME:")                                                        # test that perfect rhyme doesnt give false positives
print(BREAK_PERFECT_RHYME_YET_AGAIN)                                                    # 'Nice try Johnny boy your effort was good', 'but I have a leg up or at least a foot']
print(detect_perfect_rhyme_two_lines(BREAK_PERFECT_RHYME_YET_AGAIN[0], BREAK_PERFECT_RHYME_YET_AGAIN[1])) # Expected: False (boo! :( )

line_break()
print("TEST FOR ALLITERATION RHYME:")
print(ALLITERATION_RHYME1)
print(detect_alliteration(ALLITERATION_RHYME1[0]))

line_break()
print(ALLITERATION_RHYME2)
print(detect_alliteration(ALLITERATION_RHYME2[0]))

line_break()
print("TEST FOR ASSONANCE RHYME WITHIN LINE:")
print(ASSONANCE_RHYME)
print(detect_assonance_in_line(ASSONANCE_RHYME[0]))

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

line_break()
print("TEST SYLLABLE_WORD METHOD:")
print "hello"
print syllable_word((transcribe_string("hello")))
print len(syllable_word((transcribe_string("hello"))))  # Expected: 2 yay!
line_break()
print "this"
print syllable_word((transcribe_string("this")))
print len(syllable_word((transcribe_string("this"))))  # Expected: 3 yay!
line_break()
print "bottle"
print syllable_word((transcribe_string("bottle")))
print len(syllable_word((transcribe_string("bottle"))))  # Expected: 2 yay!
line_break()
print "is"
print syllable_word((transcribe_string("is")))
print len(syllable_word((transcribe_string("is"))))  # Expected: 3 yay!
line_break()
print "wonderful"
print syllable_word((transcribe_string("wonderful")))
print len(syllable_word((transcribe_string("wonderful"))))  # Expected: 3 yay!
line_break()
print "clocks"
print syllable_word((transcribe_string("clocks")))
print len(syllable_word((transcribe_string("clocks"))))  # Expected: 1 yay!

line_break()
print("TEST SYLLABLE_STRING METHOD:")
print("hello this bottle is wonderful")
print(syllable_string("hello this bottle is wonderful"))

line_break()
print("TEST SYLLABLE TOTAL METHOD:")
pprint.pprint(LOSE_YOURSELF)
lose_yourself_total_syllables = syllable_total(LOSE_YOURSELF)
print(lose_yourself_total_syllables)

line_break()
print("FIND SYLLABLE COUNTS OF LOSE YOURSELF")
for x in lose_yourself_total_syllables:
    print(len(x))

line_break()
print("TEST SYLLABLE TOTAL METHOD, HOL UP:")
pprint.pprint(HOL_UP)
hol_up_total_syllables = syllable_total(HOL_UP)
print(hol_up_total_syllables)

line_break()
print("FIND SYLLABLE COUNT OF HOL UP")
for x in hol_up_total_syllables:
    print(len(x))

print("TEST SYLLABLE NO BOUNDARIES:")
pprint.pprint(SAMPLE_TEXT)
print(syllable_string_no_word_boundaries(SAMPLE_TEXT))

########################
# END SYLLABLE TESTS #
########################

####################
# BEGIN FREQ TESTS #
####################

line_break()
horiz_line()
print("Mack-lemore & Jay-C Collab on Frequency Methods, Ass & All")
horiz_line()

line_break()
print("TESTING VOWEL_FREQ")
print(SAMPLE_TEXT)
print(transcribe_string(SAMPLE_TEXT))
vowel_od_1 = vowel_freq(transcribe_string(SAMPLE_TEXT))
for k, v in vowel_od_1.items():
    print k, v

line_break()
print("TESTING VOWEL FREQ MORE SERIOUSLY")
print(LOSE_YOURSELF)
print(transcribe_list(LOSE_YOURSELF))
vowel_od_2 = []
for l in LOSE_YOURSELF:
    vowel_od_2.append(vowel_freq(transcribe_string(l)))

for x in vowel_od_2:
    print("\n")
    for k, v in x.items():
        print k, v

line_break()
print("TESTING ALLITERATION_FREQ")
print(ALLITERATION_RHYME1[0])
print(transcribe_string(ALLITERATION_RHYME1[0]))
allit_od_1 = allit_freq(transcribe_string(ALLITERATION_RHYME1[0]))
for k, v in allit_od_1.items():
    print k, v

##################
# END FREQ TESTS #
##################

#####################
# BEGIN MULTI TESTS #
#####################

horiz_line()
print("TESTING MULTISYLLABIC RHYMES BRACE YOUR ASSONANCE")
horiz_line()

line_break()
print(LOSE_YOURSELF[3])
print(LOSE_YOURSELF[4])
pprint.pprint(multi_sequence(LOSE_YOURSELF[3],LOSE_YOURSELF[4]))

if (len(sys.argv) > 1):
    multi_file_swag = []
    line_break()
    file_swag = read_and_scrub_text_file(1)
    for i in range(0, len(file_swag) - 1):
        temp = multi_sequence(file_swag[i], file_swag[i + 1])
        if len(temp) != 0:
            multi_file_swag.append(temp)
    pprint(multi_file_swag)
        
###################
# END MULTI TESTS #
###################
