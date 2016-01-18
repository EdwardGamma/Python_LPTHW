# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:22:10 2016

@author: yunzhen
"""

import random   # random is a module
from urllib import urlopen   # Only Python2.x has 'urllib' module
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

for whatever in urlopen(WORD_URL).readlines():
    WORDS.append(whatever.strip()) 

snippets = PHRASES.keys()
random.shuffle(snippets)
phrase = PHRASES[snippet]

class_names = [w.capitalize() for w in   
                   random.sample(WORDS, snippet.count("%%%"))]
                   
                   
other_names = random.sample(WORDS, snippet.count("***"))

print class_names[1]
print other_names[1]