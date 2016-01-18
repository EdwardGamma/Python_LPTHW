##Word Drills
# class: Tell Python to make a new kind of thing
# instance: what you get when you tell Python to create a class
# self: the variable being accessed
# class X(Y) --- "Make a class named X that is-a Y"
# class X(object): def __ini__(self, J) --- "class X takes two parameters"
# class X(object): def F(self, J) ---"class X has a function F takes two parameters"
# foo.F(J): ---"From foo get the F function and call it with parameter'self' and 'J'"
# foo.K = Q ---"From foo get the K attribute and set it to Q"

import random   # random is a module
from urllib import urlopen   # Only Python2.x has 'urllib' module
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    # %%% --- class; *** --- function or others; @@@ --- parameters
    "class %%%(%%%):": "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" : "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":  # the second argument is "english"
    PHRASE_FIRST = True

# load up the words from the website
for whatever in urlopen(WORD_URL).readlines():
    WORDS.append(whatever.strip())    # append the elements into the 'WORDS' list
    # strip function: http://www.tutorialspoint.com/python/string_strip.htm

def convert(snippet, phrase):
    class_names = [whatever.capitalize() for whatever in   
                   random.sample(WORDS, snippet.count("%%%"))]
    # random.sample() --- Return a k length list of unique elements chosen from the sequence
    # .capitalize() returns the STRING with capitalized first character
    # equivelant to :
    # ##class_names =[]
    # ##for w in ramdom.sample(WORDS, snippet.count("%%%"))
    # ##    class_names.append(w.capitalize())
    
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []       # the result list
    
    param_names = []
    for i in range(0, snippet.count("@@@")):   # to iterate between 0 and count()
        param_count = 7      
        # or random.randint(1, 3)  # # Return a random integer <=  =>
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    
    # generates the results{} dict
    for whatever in snippet, phrase:
        # copy from the PHRASES dict
        result = whatever[:]  # a[:2] copy the first two elements; a[2:] copy all elements from the 2nd

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)  # (old, new[, max])

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        # dict.keys() returns a list  -- http://www.tutorialspoint.com/python/dictionary_keys.htm
        snippets = PHRASES.keys()  # alphabetically
        random.shuffle(snippets)   # random is a module
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            
            print question
            
            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"

