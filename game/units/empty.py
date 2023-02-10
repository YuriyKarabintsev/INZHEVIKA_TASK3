from game.units.figure import Figure


class Empty(Figure):
    def __init__(self, x, y):
        super().__init__(x, y)

