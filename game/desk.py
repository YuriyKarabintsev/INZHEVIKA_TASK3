import logging
import os

from typing import Union

try:
    from game.units import *
except ModuleNotFoundError:
    from units import *


class Desk(object):
    def __init__(self):
        logging.info("Desk created")
        self.desk = self.get_clear_desk()
        self.all = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def get_figure(self, position):
        return self.desk[position[0]][position[1]]

    def refactor_position(self, position: str) -> tuple[int, int]:
        if position[0] in self.all:
            return 8 - int(position[1]), self.all.index(position[0])
        return 8 - int(position[0]), self.all.index(position[1])

    def check_self_figure(self, position, team):
        if not isinstance(self.get_figure(position), Empty):
            if team == self.desk[position[0]][position[1]].team:
                return True
        return False

    @staticmethod
    def get_clear_desk():
        desk: list[list[Union[Empty, GameChip]]] = []
        for y in range(8):
            desk_line = []
            for x in range(8):
                desk_line.append(Empty(y, x))
            desk.append(desk_line)

        desk[0][0] = GameChip(0, 0, 1)
        desk[0][-1] = GameChip(0, 7, 2)
        desk[-1][0] = GameChip(7, 0, 3)
        desk[-1][-1] = GameChip(7, 7, 4)

        logging.info("Board cleared")

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
    _FORMAT = '[%(asctime)s] [%(levelname)s]: %(process)d %(name)s %(message)s'
    _DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    _LOG_PATH = "logs.log"

    logging.basicConfig(
        format=_FORMAT,
        datefmt=_DATE_FORMAT,
        level=logging.INFO
    )
    handler = logging.FileHandler("../" + _LOG_PATH, mode='+a')
    handler.setFormatter(logging.Formatter(_FORMAT))

    logging.getLogger().addHandler(handler)

    _desk = Desk()

    _number_of_the_player = 1

    while True:
        os.system("clear")

        _desk.show()
        _input = input("input: ")
        if _input == "exit":
            logging.info("Exit")
            break
        _pos_from, _pos_to = _input.split()
        _pos_from = _desk.refactor_position(_pos_from)
        _pos_to = _desk.refactor_position(_pos_to)
        if _desk.check_self_figure(_pos_from, _number_of_the_player):
            pass
