import pygame
import logging
#from game.desk import Desk
from graphics import Board

from config import (
    DATE_FORMAT, FORMAT, LOG_PATH
)

running = True
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Наступи на товарища")

board = Board(8, 8)

if __name__ == "__main__":

    logging.basicConfig(
        format=FORMAT,
        datefmt=DATE_FORMAT,
        level=logging.INFO
    )
    handler = logging.FileHandler(LOG_PATH, mode='+a')
    handler.setFormatter(logging.Formatter(FORMAT))
    logging.getLogger().addHandler(handler)

    logging.info("Program started")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("black"))
        board.render(screen, 1)
        pygame.display.flip()
    pygame.quit()
