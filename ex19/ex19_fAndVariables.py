# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %r 盒 of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
   
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+1+2+6+4, 58*0.4) # 23.200000000000003

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese * 1.59, amount_of_crackers / 5) # You have 15 cheeses!
