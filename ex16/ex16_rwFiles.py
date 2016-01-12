from sys import argv

script, fileName = argv

print "We're going to erase %r." % fileName
print "If you dont want that, hit CTRL-C (^C)." #Control+C aborts the application almost immediately while Control+Z shunts it into the background, suspended.
print "If you do want that, hit Enter."

raw_input("?")

print "Opening the file..."
target = open(fileName, 'w')    # get the file object

print "Truncation the file. Goodbye!"
#target.truncate()    #duplicate if open in 'w' mode

print "Now Im going to ask you for three lines."

#get user inputs
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write contents into file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#new = "%s \n%s \n%s \n" % (line1,  line2,  line3)
target.write("%s \n%s \n%s \n" % (line1,  line2,  line3))

print "And finally, we close it."
target.close()
