import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 60

    def render(self, surface, border, start_x=260, start_y=110):
        self.border = border
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(surface, pygame.Color("white"), (start_x + j * self.cell_size + self.left,
                start_y + i * self.cell_size + self.top,
                self.cell_size, self.cell_size), self.border)