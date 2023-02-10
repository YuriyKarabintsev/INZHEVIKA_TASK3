from game.units.figure import Figure


class GameChip(Figure):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)

    def __str__(self):
        return "{0}{1}".format(self.team, self.rang)
