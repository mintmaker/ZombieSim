import random
import numpy as np
import warnings

#Global Variables
MAP_SIZE = (301, 301)


class Map: #TODO: add go functions, and ovethink format
    '''
    The Map object handles as the map and here is the information of the simulation stored

    Args:
    size : tuple
        The arg defines the size of the map

    Attributes:
    size : tuple
        size of the map
    numpy : numpy.array
        represents the current map
    '''


    def __init__(self,
                 size,
                 mode='yx',
                 ENC_HUMAN=1,
                 ENC_ZOBIE=2,
                 ENC_NULL=0):
        self.mode = mode
        if mode == 'xy':
            self.size = size
        elif mode == 'yx':
            self.size = (size[1], size[0])
        else:
            raise TypeError(f'Excpected yx or xy, got {mode}')

        self.ENC_HUMAN = ENC_HUMAN
        self.ENC_ZOMBIE = ENC_ZOBIE
        self.ENC_NULL= ENC_NULL
        #self.numpy = np.zeros((self.size[0],self.size[1], 2), dtype=np.int32) # Version with multiple objects in one field
        self.numpy = np.zeros(self.size)
        self.ids = {}

    def add_humans(self, **kwargs):
        if 'positions' in kwargs.keys():
            if isinstance(kwargs['positions'], np.array):
                for i in kwargs['positions']:
                    if self.numpy[i[0]][i[1]]):
                        raise TypeError('arg \'positions\' is empty')
        elif 'method' in kwargs.keys() and 'nb' in kwargs.keys():
            pass
        else:
            raise TypeError('no correct kwargs')

    def add_zombies(self, **kwargs):
        if 'positions' in kwargs.keys():
            pass
        elif 'method' in kwargs.keys() and 'nb' in kwargs.keys():
            pass
        else:  # Some bug here
            raise TypeError('no correct kwargs')

    def human_up(self, y, x):
        next_x, next_y = (x, y)
        if not ( self.numpy[y][x] == self.ENC_HUMAN):
            self.numpy[y][x]= self.ENC_NULL
            self.numpy[next_y][next_x] = self.ENC_HUMAN

if __name__ == '__main__':
    map = Map(size=(301, 301))
    map.add_humans(p=1)
