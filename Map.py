import random
import numpy as np
import warnings

#Global Variables
MAP_SIZE = (301, 301)


class Map:
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
