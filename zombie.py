"""

by TeamCoder
Special Thanks to Danny

"""


import random
import numpy as np

#Global Variables
MAP_SIZE = (301, 301)


class Map:
    def __init__(self, size):
        self.size = size
        self.values = np.zeros(self.size)

    def __getitem__(self, item):
        return self.values[item]



class World:

    def __init__(self,
                 size : tuple,
                 humans : tuple,
                 zombies : tuple
                 ):



if __name__ == '__main__':
    map = Map(MAP_SIZE)
    print(map[10][10])