try:
    from game.units.figure import Figure
except ModuleNotFoundError:
    from units.figure import Figure


class GameChip(Figure):
    def __init__(self, team, rang: int = 1):
        super().__init__(team, rang)

    def __str__(self):
        return "{0}{1}".format(self.team, self.rang)

    def __copy__(self):
        return GameChip(self.team, self.rang)
