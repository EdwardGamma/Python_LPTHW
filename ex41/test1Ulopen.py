# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:54:24 2016

@author: yunzhen
"""
import random   # random is a module
from urllib import urlopen   # Only Python2.x has 'urllib' module
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip()) 

print WORDS