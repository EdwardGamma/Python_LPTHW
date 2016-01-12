# ask user which file to open

from sys import argv

script, filename = argv

print "Here is your file %s:" % filename
txt = open(filename)    #returns a file object
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
