'''
  File name: rmHorSeam.py
'''

import numpy as np
from PIL import Image
from cumMinEngHor import cumMinEngHor

from rmVerSeam import rmVerSeam


def rmHorSeam(I, My, Tby):
    Ix, Ex = rmVerSeam(np.transpose(I, axes=(1, 0, 2)), np.transpose(My), np.transpose(Tby))
    Iy = np.transpose(Ix, axes=(1, 0, 2))
    E = np.transpose(Ex)
    return Iy, E
