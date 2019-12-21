"""

by TeamCoder
Special Thanks to Danny

"""


import random
import numpy as np
import warnings
from Map import Map

#Global Variables
MAP_SIZE = (301, 301)


class World:
    '''
    The World object handles as the world in the simlation and is used as an simulation itself.

    Parameters
    ----------
    size : tuple (int, int)
        size of the simulated city
    humans : tuple (int, str/list/numpy.array/tuple)
        first item is the number of zombies and the second item describes the positioning method or positions
    humans tuple (int, str/list/numpy.array/tuple)
        first item is the number of zombies and the second item describes the positioning method or positions

    Attributes
    ----------
    size : tuple
        size of the map of the simulation
    nb_humans : int
        number of humans at the beginning of the simulation
    nb_zombies : int
        This is the number of zombies at the beginning of the simulation
    humans_positions : numpy.array
        represents the positions of the humans
    zombies_positions : numpy.array
        represents the positions of the zombies
    '''

    def __init__(self,
                 size : tuple = (100, 100),
                 humans : tuple = (5000, 'random'),
                 zombies : tuple = (1, 'middle'),
                 ):
        self.size = size
        self.nb_humans = humans[0]
        self.nb_zombies = zombies[0]

        self.map = Map(size=self.size)

        if isinstance(humans[1], str):
            pass

        if isinstance(humans[1], tuple) or isinstance(humans[1], list) or isinstance(humans[1], np.ndarray):
            self.human_positions = np.array(humans[1])
            self.map.add_humans(positions=self.human_positions)










if __name__ == '__main__':
    map = Map(MAP_SIZE)
    world = World(humans=(5000, np.zeros((5000, 1))))
    #print(map[10][10])
    print('hi')