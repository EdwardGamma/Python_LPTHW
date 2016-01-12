x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Traceback (most recent call last):
#   File "ex6.py", line 4, in <module>
#     y = "Those who know %d and those who %s." % (binary, do_not)
# TypeError: %d format: a number is required, not str


print x
print y

# %r displays raw data, is good for debugging
print "I said: %r." % x

# single-quote inside a string that has double-quotes
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w+e
