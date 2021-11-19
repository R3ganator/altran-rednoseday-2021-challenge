from directions import *


class Decipher:
    def __init__(self):
        self.f = open("Alexander_input.txt", "r")
        self.keypad = np.arange(1, 10).reshape(3, 3)
        self.g = open("Alexander_answer.txt", "w")

    def main(self):
        code = []
        start = self.keypad[1, 1]
        new = []
        num = start
        for line in self.f:
            for dir in line:
                if dir == "U":
                    new = up(inst, num)
                    num = self.keypad[new[0], new[1]]
                elif dir == "D":
                    new = down(inst, num)
                    num = self.keypad[new[0], new[1]]
                elif dir == "L":
                    new = left(inst, num)
                    num = self.keypad[new[0], new[1]]
                elif dir == "R":
                    new = right(inst, num)
                    num = self.keypad[new[0], new[1]]
            code.append(num)
        self.g.write(str(code))


if __name__ == '__main__':
    inst = Decipher()
    inst.main()
