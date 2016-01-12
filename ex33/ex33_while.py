# a while loop has to have a False condition where the loop can terminate

i = 1
numbers = []

#while i < 6:
#    print "At the top i is %d" % i
#    print "The next element is %d" % (i+1)
#    
#    numbers.append(i)
#    
#    i = i + 1
#    
#    # Numbers now:  [-1, 0, 1, 2, 3, 4] Finished
#    print "Numbers now: ",numbers, "Finished"  
#    
#    print "At the bottom i is %d" % i
#    
#    
#print "The numbers: "
#
#for dehhhh in numbers:
#    print dehhhh

def appendList(i):
        print "The current index is %d" % i
        numbers.append(i)
        
m = int(raw_input("Please enter the number of elements:  "))

while i <= m:
    
    appendList(i)
    i += 1

print "The list is: "

for dehhh in numbers:    
    print dehhh
        
        
