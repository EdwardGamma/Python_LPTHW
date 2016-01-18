from sys import exit    # sys.exit()
from random import randint

class Scene(object):   # 1st top level class
    
    def enter(self):
        pass
        
class Engine(object):  # 2nd top level class
    
    def __init__(self, scene_map):
        pass
        
        #print """Aliens have invaded a space ship and you has to go through a maze of rooms defeating them so you can escape into an escape pod to the planet below. """

        
    def play(self):
        pass
        
class Death(Sence):
    
    def enter(self):
        pass
        
class CentralCorridor(Scene):

    def enter(self):
        pass
        
class LaserWeaponArmory(Scene):

    def enter(self):
        pass
        
class TheBridge(Scene):
    
    def enter(self):
        pass
        
class EscapePod(Scene):

    def enter(self):
        pass
        
class Map(object):      # 3rd top level class
    
    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
        
a_map = ('central_corridor')
a_game = Engine(a_map)
a_game.play()





