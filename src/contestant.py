import random


class Contestant:

    def __init__(self, switch=False):
        self.switch = switch
        self.selection = None

    def select_door(self, door_count):
        self.selection = int(random.uniform(0, door_count))
        return self.selection

    def wanna_switch(self, new_door):
        if self.switch:
            return new_door
        else:
            return self.selection
