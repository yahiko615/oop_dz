from abc import ABC, abstractmethod


class IShip(ABC):
    """Abstract class for a ship."""

    @abstractmethod
    def is_sunk(self):
        """Check if the ship has been sunk."""
        pass
