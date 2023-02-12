import logging
import os
import random

from copy import copy
from typing import Union
from threading import Thread

try:
    from game.units import *
except ModuleNotFoundError:
    from units import *


class Desk(object):
    def __init__(self):
        logging.info("Desk created")
        self.desk = self.get_clear_desk()
        self.all = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.team_spawns = {1: (0, 0), 2: (7, 0), 3: (0, 7), 4: (7, 7)}

    def get_figure(self, position):
        return self.desk[position[0]][position[1]]

    def refactor_position(self, position: str) -> tuple[int, int]:
        if position[0] in self.all:
            return 8 - int(position[1]), self.all.index(position[0])
        return 8 - int(position[0]), self.all.index(position[1])

    def check_self_figure(self, position, team):
        logging.info(position)
        if not isinstance(self.get_figure(position), Empty):
            if team == self.desk[position[0]][position[1]].team:
                return True
        return False

    @staticmethod
    def get_possible_moves(xchip: int, ychip: int, direction: str, distance: int, result=None):
        r"""

        :param result:
            result
        :param xchip:
            x coordinate (max = 7)
        :param ychip:
            x coordinate (max = 7)
        :param direction:
            direction of calculation:
            up, down, left, right
        :param distance:
            travel distance (max = 6)
        :return: list
        """
        if result is None:
            result = []
        possible_moves = []

        if (xchip > 7 or xchip < 0) or (ychip > 7 or ychip < 0):
            return []
        if direction == "down":
            i = 0
            while ychip != ychip - distance and 0 <= ychip <= 7:
                if 0 <= xchip - (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip - (distance - i), ychip))
                if 0 <= xchip + (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip + (distance - i), ychip))
                i += 1
                ychip += 1
        elif direction == "up":
            i = 0
            while ychip != ychip + distance and 0 <= ychip <= 7:
                if 0 <= xchip - (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip - (distance - i), ychip))
                if 0 <= xchip + (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip + (distance - i), ychip))
                i += 1
                ychip -= 1
        elif direction == "left":
            i = 0
            while xchip != xchip - distance and 0 <= xchip <= 7:
                if 0 <= ychip - (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip, ychip - (distance - i)))
                if 0 <= ychip + (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip, ychip + (distance - i)))
                i += 1
                xchip += 1
        else:
            i = 0
            while xchip != xchip + distance and 0 <= xchip <= 7:
                if 0 <= ychip - (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip, ychip - (distance - i)))
                if 0 <= ychip + (distance - i) <= 7 and distance - i >= 0:
                    possible_moves.append((xchip, ychip + (distance - i)))
                i += 1
                xchip -= 1

        result.extend(possible_moves)

    def get_all_possible_moves(self, xchip: int, ychip: int, distance: int):
        all_moves = []
        t1 = Thread(target=self.get_possible_moves, args=(xchip, ychip, "right", distance, all_moves))
        t2 = Thread(target=self.get_possible_moves, args=(xchip, ychip, "down", distance, all_moves))
        t3 = Thread(target=self.get_possible_moves, args=(xchip, ychip, "up", distance, all_moves))
        t4 = Thread(target=self.get_possible_moves, args=(xchip, ychip, "left", distance, all_moves))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t1.join()
        t1.join()
        t1.join()
        return all_moves

    @staticmethod
    def get_clear_desk():
        desk: list[list[Union[Empty, GameChip]]] = []
        for y in range(8):
            desk_line = []
            for x in range(8):
                desk_line.append(Empty())
            desk.append(desk_line)

        desk[0][0] = GameChip(1)
        desk[0][-1] = GameChip(2)
        desk[-1][0] = GameChip(3)
        desk[-1][-1] = GameChip(4)

        logging.info("Board cleared")

        return desk

    def do_move(self, from_position, to_position):
        figure = self.get_figure(from_position)
        self.desk[to_position[0]][to_position[1]] = copy(figure)
        if from_position != self.team_spawns[figure.team]:
            self.desk[from_position[0]][from_position[1]] = Empty()

    @staticmethod
    def reverse_position(position: tuple):
        return tuple(reversed(position))

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
    _distance = random.randint(1, 6)

    while True:
        os.system("clear")
        _desk.show()
        _input = input(f"input ({_distance}, {_number_of_the_player}): ")
        if _input == "exit":
            logging.info("Exit")
            break
        _pos_from, _pos_to = _input.split()
        _pos_from = _desk.refactor_position(_pos_from)
        _pos_to = _desk.refactor_position(_pos_to)
        print(repr(_desk.get_figure((_pos_from[1], _pos_from[0]))))
        print(repr(_desk.get_figure((_pos_to[1], _pos_to[0]))))
        if _desk.check_self_figure(_pos_from, _number_of_the_player):
            if _desk.reverse_position(_pos_to) in _desk.get_all_possible_moves(_pos_from[1], _pos_from[0], _distance):
                _desk.do_move(_pos_from, _pos_to)
                if _number_of_the_player + 1 == 5:
                    _number_of_the_player = 1
                else:
                    # _number_of_the_player += 1
                    pass
                _distance = random.randint(1, 6)
            else:
                logging.error("BAD POSITION")
        else:
            logging.error("BAD SELF FIGURE")
