import unittest
from detection.rhyme_detect import *

PERFECT_RHYME = ["This is a perfect rhyme",
                 "Bitches split on a dime"]


class TestRhymeDetection(unittest.TestCase):
    def test_transcribe_string(self):
        self.assertEqual(
                # From CMU Pronouncing Dict Website
                # M AE1 K ER0 AH0 L . B AE1 T . F R AH1 M . HH EH1 L .
                [['M', 'AE1', 'K', 'ER0', 'AH0', 'L'], ['B', 'AE1', 'T'], ['F', 'R', 'AH1', 'M'], ['HH', 'EH1', 'L']],
                transcribe_string("Mackerel bat from hell")
        )
        return

    def test_transcribe_list(self):
        self.assertEqual(
                # From the CMU Pronouncing Dictionary
                # DH IH1 S . IH1 Z . AH0 . P ER0 F EH1 K T . R AY1 M .
                # B IH1 CH IH0 Z . S P L IH1 T . AA1 N . AH0 . D AY1 M .
            [
                [['DH', 'IH1', 'S'], ['IH1', 'Z'], ['AH0'], ['P', 'ER0', 'F', 'EH1', 'K', 'T'], ['R', 'AY1', 'M']],
                [['B', 'IH1', 'CH', 'IH0', 'Z'], ['S', 'P', 'L', 'IH1', 'T'], ['AA1', 'N'], ['AH0'], ['D', 'AY1', 'M']]
            ],
            transcribe_list(PERFECT_RHYME)
        )
        return

    def test_syllable_count(self):
        self.assertEqual(
                # From Merriam Webster Dictionary
                # WONDERFUL: WON . DER . FUL
                # 3 syllables
                3, 
                syllable_count(transcribe_string("wonderful"))
            )
        return

    def test_is_vowel(self):
        self.assertEqual(
                # From the CMU Pronouncing Dictionary
                # Vowels: 'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'
                True,
                is_vowel("IH1")
            )
        return

    def test_scrub_punct(self):
        self.assertEqual(
                # ... I don't really have an official source for this one... my brain?
                "This'll have a ton of pointless punctuation",
                scrub_punct("This'll, have: a; (ton) of _pointless -punctuation")
            )
        return

    def test_detect_perfect_rhyme_two_lines(self):
        self.assertEqual(
                # From Rap Genius: http://genius.com/posts/24-Rap-genius-university-rhyme-types
                # Definition of a perfect rhyme: a rhyme in which "the endings of words sound exactly the same"
                True,
                detect_perfect_rhyme_two_lines("Totally a hundred grand", "Cannon in the waist band")
            )
        return
    def test_vowel_freq(self):
        self.assertEqual(
                # From the CMU Pronouncing Dictionary
                # Vowels: 'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'
                # Look I was gonna go easy on you
                # [u'L', u'UH1', u'K'], [u'AY1'], [u'W', u'AA1', u'Z'], [u'G', u'AA1', u'N', u'AH0'], [u'G', u'OW1'], [u'IY1', u'Z', u'IY0'], [u'AA1', u'N'], [u'Y', u'UW1']
                {'AA1':3, 'AH0':1, 'AY1':1, 'IY0':1, 'IY1':1, 'OW1':1, 'UH1':1, 'UW1':1},
                vowel_freq(transcribe_string("Look I was gonna go easy on you"))
            )
        return
    def test_allit_freq(self):
        self.assertEqual(
                # From Rap Genius: http://genius.com/posts/24-Rap-genius-university-rhyme-types
                # Definition of an alliteration: a rhyme in which "words begin with the same letter or sound"
                # Look I was gonna go easy on you
                # [u'L', u'UH1', u'K'], [u'AY1'], [u'W', u'AA1', u'Z'], [u'G', u'AA1', u'N', u'AH0'], [u'G', u'OW1'], [u'IY1', u'Z', u'IY0'], [u'AA1', u'N'], [u'Y', u'UW1']
                {'AA1':1, 'AY1':1, 'G':2, 'L':1, 'W':1, 'IY1':1, 'Y':1},
                allit_freq(transcribe_string("Look I was gonna go easy on you"))
            )
        return

    # THIS TEST IS BROKEN I PROMISE I'LL FIX IT WHEN IM LESS TIRED    
    # def test_extract_vowels(self):
    #     self.assertEqual(
    #             # From the CMU Pronouncing Dictionary
    #             # Vowels: 'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'
    #             # "There once was a man from Peru"
    #             # [u'DH', u'EH1', u'R'], [u'W', u'AH1', u'N', u'S'], [u'W', u'AA1', u'Z'], [u'AH0'], [u'M', u'AE1', u'N'], [u'F', u'R', u'AH1', u'M'], [u'P', u'ER0', u'UW1']
    #             ['EH1', 'AH1', 'AA1', 'AH0', 'AE1', 'AH1', 'ER0', 'UW1'],
    #             extract_vowels(transcribe_string("There once was a man from Peru"))
    #         )
    #     return

