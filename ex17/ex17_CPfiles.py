from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
# indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit Enter to continue, CTRL-C to abort."

raw_input("So??????????????????????")
raw_input("Have you decided yet")
raw_input("Really????")

out_file = open(to_file, 'w')
out_file.write(indata)

print 'Alright, all done.'

out_file.close() # call f.close() to close it and free up any system resources taken up by the open file.
in_file.close()
