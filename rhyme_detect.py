#!/usr/bin/python

import nltk
from nltk.corpus import cmudict

# Sample rhymes
# Lose Yourself - Eminem

#lose_yourself = "His palms are sweaty, knees weak, arms are heavy
#        There's vomit on his sweater already, mom's spaghetti
#        He's nervous, but on the surface he looks calm and ready to drop bombs,
#        But he keeps on forgetting what he wrote down,
#        The whole crowd goes so loud
#        He opens his mouth, but the words won't come out"

perfect_rhyme = "This is a perfect rhyme \n bitches turn on a dime"

sample_text = "Mackerel bat from hell"

transcr = cmudict.dict()

results = [transcr[w][0] for w in sample_text.lower().split()]

print(results)


