try:
    from game.units.figure import Figure
except ModuleNotFoundError:
    from units.figure import Figure


class Empty(Figure):
    def __init__(self):
        super().__init__()

