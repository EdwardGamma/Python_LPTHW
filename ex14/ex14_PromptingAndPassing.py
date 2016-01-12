# use argv and raw_input together to ask the user something specific

from sys import argv

user_name, script = argv
prompttttt = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n' + '>'

print "Hi %s, I'm the %s script." % (script, user_name)   # two variables with brackets
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompttttt)

print "Where do you live %s?" % user_name
lives = raw_input(prompttttt)

print "What kind of computer do you have?"
computer = raw_input(prompttttt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
