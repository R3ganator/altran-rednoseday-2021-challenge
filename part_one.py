import numpy as np
from Directions import *


class Code:
    def __init__(self):
        self.f = open("Alexander_input.txt", "r")
        self.keypad = np.arange(1, 10).reshape(3, 3)

    def find(self, numb):
        result = np.where(self.keypad == numb)
        list_coord = list(zip(result[0], result[1]))
        coord = None
        for coord in list_coord:
            coord = list(coord)
        return coord


if __name__ == '__main__':
    inst = Code()
    code = []
    start = inst.keypad[1, 1]
    new = []
    num = start
    for line in inst.f:
        for dir in line:
            if dir == "U":
                new = up(num)
            elif dir == "D":
                new = down(num)
            elif dir == "L":
                new = left(num)
            elif dir == "R":
                new = right(num)
            num = new
        code.append(num)
    print(code)
