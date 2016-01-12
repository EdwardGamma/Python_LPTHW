def break_words(stuff):
    """This function will break up words for us."""  # Documentation strings
    words = stuff.split(' ')   # http://www.tutorialspoint.com/python/string_split.htm
    return words
    # >>> help(ex25_Practice2.break_words)
    # break_words(stuff)
    #   This function will break up words for us.
    # (END)

    
# run
# >>>python
# >>>import ex25_Practice2
# >>>sentence = "All good things come to those who wait."
# >>>words = ex25_Practice2.break_words(sentence)
# >>>words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    
def print_first_word(words):
    """Prints the first word after popping if off."""
    word = words.pop(0)   # will be removed after popping off
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    # pop(-1) print out the last item of the list
    word = words.pop(-1)   # new list after the previous pop operation
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_works(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
