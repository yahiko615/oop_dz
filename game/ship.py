from igame.iship import IShip


class GameShip(IShip):
    """Represents a ship."""

    def __init__(self, name, size):
        """Initialize the ship"""
        self.name = name
        self.size = size
        self.positions = []
        self.hit_count = 0

    def is_sunk(self):
        """Check if the ship has been sunk."""
        return self.hit_count == self.size
