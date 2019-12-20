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
        self.numpy = np.zeros(self.size)

    def set_humans(self, **kwargs):
        if 'positions' in kwargs.keys():
            pass
        elif 'method' in kwargs.keys() and 'nb' in kwargs.keys():
            pass
        else:
            raise 'Warning:hi'


class World:
    '''
    The World object handles as the world in the simlation and is used as an simulation itself.

        Args:
            size (tuple): The arg defines the size of the simulated city
            humans (tuple): The arg defines in with first item the number of humans and with the second one the positions or the method for positioning.
            humans (tuple): The arg defines in with first item the number of zombies and with the second one the positions or the method for positioning.

        Attributes:
            arg (str): This is where we store arg,
        '''
    def __init__(self,
                 size : tuple = (100, 100),
                 humans : tuple = (5000, 'random'),
                 zombies : tuple = (1, 'middle'),
                 ):
        self.size = size
        self.nb_humnas = humans[0]
        self.nb_zombies = zombies[0]
        if np.array(humans[1]).shape == self.nb_humnas:
            self.positions = np.array(humans[1])


        if isinstance(humans[1], str):










if __name__ == '__main__':
    map = Map(MAP_SIZE)
    world = World()
    #print(map[10][10])