import numpy as np
from main import *


def find(inst, numb):
    result = np.where(inst.keypad == numb)
    list_coord = list(zip(result[0], result[1]))
    coord = None
    for coord in list_coord:
        coord = list(coord)
    return coord


def up(inst, numb):
    coord = find(inst, numb)
    if coord[0] != 0:
        coord[0] = coord[0] - 1
    return coord


def down(inst, numb):
    coord = find(inst, numb)
    if coord[0] != 2:
        coord[0] = coord[0] + 1
    return coord


def left(inst, numb):
    coord = find(inst, numb)
    if coord[1] != 0:
        coord[1] = coord[1] - 1
    return coord


def right(inst, numb):
    coord = find(inst, numb)
    if coord[1] != 2:
        coord[1] = coord[1] + 1
    return coord
