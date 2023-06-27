import random

from igame.iboard import IBoard


class GameBoard(IBoard):
    """Represents the game board. """

    def __init__(self):
        """Initialize the board with empty cells and an empty list of ships."""
        self.board_size = 10
        # self.board_status = board_status
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = []

    def __str__(self):
        """Return a string representation of the board."""
        board_str = '  | ' + ' | '.join(str(i) for i in range(self.board_size)) + ' |\n'
        for row_num, row in enumerate(self.board):
            row_str = ' | '.join(cell for cell in row)
            board_str += f'{row_num} | {row_str} |\n'
        return board_str

    def place_ship(self, ship):
        """Place a ship on the board."""
        ship_size = ship.size
        while True:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - ship_size)
                # positions = [(row, col - i) for i in range(ship_size)]
                positions = [(row, col + i) for i in range(ship_size)]
            else:
                row = random.randint(0, self.board_size - ship_size)
                col = random.randint(0, self.board_size - 1)
                positions = [(row + i, col) for i in range(ship_size)]
            if all(self.board[r][c] == ' ' for r, c in positions):
                ship.positions = positions
                self.ships.append(ship)
                for r, c in positions:
                    self.board[r][c] = '♦'
                break

    def receive_attack(self, row, col):
        """Process an attack at the specified row and column."""
        cell = self.board[row][col]
        if cell == ' ':
            print("You missed!")
            self.board[row][col] = 'O'
        elif cell == '♦':
            for ship in self.ships:
                if (row, col) in ship.positions:
                    ship.hit_count += 1
                    if ship.is_sunk():
                        print(f"You sank the {ship.name}!")
                        self.board[row][col] = 'X'
                    else:
                        print("You hit a ship!")
                        self.board[row][col] = 'X'
                    break
        else:
            print("You already targeted that location! Choose anoher!")

    def is_game_over(self):
        """Check if all the ships on the board have been sunk."""
        return all(ship.is_sunk() for ship in self.ships)
