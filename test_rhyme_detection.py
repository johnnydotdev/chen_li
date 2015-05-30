import unittest
from detection.rhyme_detect import *

MACKEREL = "Mackerel bat from hell"

class TestRhymeDetection(unittest.TestCase):
    def test_transcribe_string(self):
        self.assertEqual(
            # From CMU Pronouncing Dict Website
            # M AE1 K ER0 AH0 L . B AE1 T . F R AH1 M . HH EH1 L .
            [['M', 'AE1', 'K', 'ER0', 'AH0', 'L'], ['B', 'AE1', 'T'], ['F', 'R', 'AH1', 'M'], ['HH', 'EH1', 'L']],
            transcribe_string(MACKEREL)
        )
