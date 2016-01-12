# define and functions

# this one is like your scripts with argv
def print_two(*arrrgs):    # function name can only have char and _
    arg1, arg2 = arrrgs
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *arrrgs is actually pointless, we can just do this
# ()::::::::::::::::::::::::
def print_two_again(arrrrg1, arrg2):
    print "arg1: %r, arrg2: %r" % (arrrrg1, arrg2)

# this just takes one argument
def print_one(a):
    print "argument 1: %r" % (a)

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("1st", "2nd")
print_two_again("1st again", "2nd again")
print_one('''just first one''')
print_none()
