class Figure(object):
    def __init__(self, team: int = 0, rang: int = 1):
        self.team = team
        self.rang = rang
        # print(self.x, self.y)

    def __repr__(self):
        return f"{self.__module__}(team={self.team}, rang={self.rang})"

    def __str__(self):
        return "--"

    def __copy__(self):
        return Figure(self.team, self.rang)
