# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:59:23 2016
Ask the user which file to open
@author: yunzhen
"""

from sys import argv

scriptName, fileName = argv

print "Here is your file %s:" % fileName
print open(fileName).read()   # txt = open(fileName)   print txt.read()
