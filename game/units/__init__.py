try:
    from game.units.chip import GameChip
    from game.units.empty import Empty
except ModuleNotFoundError:
    from units.chip import GameChip
    from units.empty import Empty

__all__ = (
    "GameChip", "Empty"
)
