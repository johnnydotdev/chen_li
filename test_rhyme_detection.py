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

