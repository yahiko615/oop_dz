from abc import ABC, abstractmethod


class IBoard(ABC):
    """Abstract class for the game board."""

    @abstractmethod
    def __str__(self):
        """Return a string representation of the board."""
        pass

    @abstractmethod
    def place_ship(self, ship):
        """Place a ship on the board."""
        pass

    @abstractmethod
    def receive_attack(self, row, col):
        """Process an attack at the specified row and column."""
        pass

    @abstractmethod
    def is_game_over(self):
        """Check if all the ships on the board have been sunk."""
        pass
