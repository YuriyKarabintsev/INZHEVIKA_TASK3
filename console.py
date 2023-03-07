import logging
import os
import random

from game.desk import Desk


if __name__ == "__main__":
    FORMAT = '[%(asctime)s] [%(levelname)s]: %(process)d %(name)s %(message)s'
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    LOG_PATH = "logs.log"

    logging.basicConfig(
        format=FORMAT,
        datefmt=DATE_FORMAT,
        level=logging.INFO
    )
    handler = logging.FileHandler("../" + LOG_PATH, mode='+a')
    handler.setFormatter(logging.Formatter(FORMAT))

    logging.getLogger().addHandler(handler)

    desk = Desk()

    number_of_the_player = 1
    distance = random.randint(1, 6)

    while True:
        os.system("clear")
        desk.show()
        input_position = input(f"input ({distance}, {number_of_the_player}): ")
        if input == "exit":
            logging.info("Exit")
            break
        pos_from, pos_to = input_position.split()
        pos_from = desk.refactor_position(pos_from)
        pos_to = desk.refactor_position(pos_to)
        print(repr(desk.get_figure((pos_from[1], pos_from[0]))))
        print(repr(desk.get_figure((pos_to[1], pos_to[0]))))
        if desk.check_self_figure(pos_from, number_of_the_player):
            if desk.reverse_position(pos_to) in desk.get_all_possible_moves(
                    pos_from[1], pos_from[0], distance
            ):
                desk.do_move(pos_from, pos_to)
                if number_of_the_player + 1 == 5:
                    number_of_the_player = 1
                else:
                    number_of_the_player += 1
                distance = random.randint(1, 6)
            else:
                logging.error("BAD POSITION")
        else:
            logging.error("BAD SELF FIGURE")
