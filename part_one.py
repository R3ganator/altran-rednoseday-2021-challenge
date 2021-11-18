import numpy as np


class Code:
    def __init__(self):
        self.inst = open("Alexander_input.txt", "r")
        self.keypad = np.arange(1, 10).reshape(3, 3)

    def find(self, num):
        result = np.where(self.keypad == num)
        list_coord = list(zip(result[0], result[1]))
        coord = None
        for coord in list_coord:
            coord = list(coord)
        return coord

    def up(self, num):
        coord = self.find(num)
        if coord[0] != 0:
            coord[0] = coord[0] - 1
        return coord

    def down(self, num):
        coord = self.find(num)
        if coord[0] != 2:
            coord[0] = coord[0] + 1
        return coord

    def left(self, num):
        coord = self.find(num)
        if coord[1] != 0:
            coord[1] = coord[1] - 1
        return coord

    def right(self, num):
        coord = self.find(num)
        if coord[1] != 2:
            coord[1] = coord[1] + 1
        return coord

    # for line in inst:
    #     start = keypad[1, 1]
    #     print(start)
    #     for dir in line:
    #         if dir == "U":



    # print(keypad[0, 2])
