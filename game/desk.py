import logging
from typing import Any

from game.units import *


class Desk(object):
    def __init__(self):
        self.desk = self.get_clear_desk()
        logging.info("Desk created")

    @staticmethod
    def get_clear_desk():
        desk: list[list[Any]] = []
        for y in range(8):
            desk_line = []
            for x in range(8):
                desk_line.append(Empty(y, x))
            desk.append(desk_line)

        desk[0][0] = GameChip(0, 0, 1)
        desk[0][-1] = GameChip(0, 0, 2)
        desk[-1][0] = GameChip(0, 0, 3)
        desk[-1][-1] = GameChip(0, 0, 4)

        logging.info("board cleared")

        return desk

    def show(self):
        print("-------------------------------------")
        for x in range(len(self.desk)):
            print(f"{7 - x + 1}|\t", end="")
            for y in range(len(self.desk[0])):
                print(self.desk[x][y], sep="\t", end="\t")
            print("|")

        print("-------------------------------------")
        print(*["\ta", "b", "c", "d", "e", "f", "g", "h"], sep="\t")


if __name__ == "__main__":
    _desk = Desk()
    _desk.show()
    