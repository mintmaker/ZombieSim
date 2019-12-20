"""

by TeamCoder
Special Thanks to Danny

"""


import random
import numpy as np
import warnings

#Global Variables
MAP_SIZE = (301, 301)


class Map:
    '''
    The Map object handles as the map, you can get the information about the current sistuation

        Args:
            size (tuple): The arg defines the size of the map

        Attributes:
            size (tuple): This is the size of the map
            numpy (numpy.array): The numpy.array represents the current map
    '''
    def __init__(self, size):
        self.size = size
        self.numpy = np.zeros(self.size)

    def add_humans(self, **kwargs):
        if 'positions' in kwargs.keys():
            pass
        elif 'method' in kwargs.keys() and 'nb' in kwargs.keys():
            pass
        else: # Some bug here
            warnings.warn(f'You don\'t have specified any of the needed args (positions, method, nb), you specified {list(kwargs.keys())}', UserWarning)


class World:
    '''
    The World object handles as the world in the simlation and is used as an simulation itself.

        Args:
            size (tuple): The arg defines the size of the simulated city
            humans (tuple): The arg defines in with first item the number of humans and with the second one the positions or the method for positioning.
            humans (tuple): The arg defines in with first item the number of zombies and with the second one the positions or the method for positioning.

        Attributes:
            size (tuple): This is the size of the map of the simulation
            nb_humans (int): This is the number of humans at the begging of the simulation
            nb_zombies (int): This is the number of zombies at the begging of the simulation
            humans_positions (numpy.array): This numpy array represents the positions of the humans
            zombies_positions (numpy.array): This numpy array represents the positions of the zombies
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