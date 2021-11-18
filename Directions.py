from part_one import *


def up(numb):
    coord = inst.find(numb)
    if coord[0] != 0:
        coord[0] = coord[0] - 1
    return coord


def down(numb):
    coord = inst.find(numb)
    if coord[0] != 2:
        coord[0] = coord[0] + 1
    return coord


def left(numb):
    coord = inst.find(numb)
    if coord[1] != 0:
        coord[1] = coord[1] - 1
    return coord


def right(numb):
    coord = inst.find(numb)
    if coord[1] != 2:
        coord[1] = coord[1] + 1
    return coord
