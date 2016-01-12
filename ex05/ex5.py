name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %s pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cooffe." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %d." %(
    age, height, weight, age + height + weight)
    
    
# Python String Formatting
class Cheese(float):
    def __str__(self):
        return 'Muenster'
    def __repr__(self):
        return 'Stilton'

chunk = Cheese(-123.4)

print(str(chunk))
# Muenster
print(repr(chunk))
# Stilton
print(int(chunk))
# -123
print('%s\t%r\t%d'%(chunk, chunk, chunk))
# Muenster  Stilton -123
