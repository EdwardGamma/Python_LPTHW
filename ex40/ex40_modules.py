# mystuff['apple']    # get apple from dict
# mystuff.apple()     # get apple from the module
# mystuff.tangerine   # same thing, it's just a variable


# Three ways to get things from things:

#   dict style
##  mystuff['apples']

#   module style
##  mystuff.apples()
##  print mystuff.tangerine

#   class style
##  thing = MyStuff()
##  thing.apple()
##  print thing.tangering

# python treats a.test("hello") as test(a, "hello"), hence there are two arguments


class Song(object):    # has to be "object"

# if became "def __init__(self)", the result would be __init__() takes exactly 1 argument (2 given)

    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for whatever in self.lyrics:
            print whatever
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
