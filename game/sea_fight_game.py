import random

from board import GameBoard
from ship import GameShip

SHIP_TYPES = {
    'Patrol Boat': 2,
    'Submarine': 3,
    'Destroyer': 3,
    'Battleship': 4,
    'Aircraft Carrier': 5
}

BOARD_SIZE = 10


class Game:
    """Represents the Sea Battle game."""

    def __init__(self):
        """Initialize the game with player's and computer's boards and the turn count."""
        self.__player_board = GameBoard()
        self.__computer_board = GameBoard()

    def play(self):
        """Start the game and play until there is a winner."""
        self.__place_ships()
        print("YOu started Sea Battle. Let's play!")
        print("The computr has placed its ships. Attack!")
        while not self.__player_board.is_game_over() and not self.__computer_board.is_game_over():
            print("\nPlayers Turn")
            print("==============")
            print("Computers Board:")
            print(self.__computer_board)
            self.__player_attack()
            if self.__computer_board.is_game_over():
                break
            print("\nComputer's Turn")
            print("================")
            self.__computer_attack()
        self.__print_game_result()

    def __place_ships(self):
        """Place the ships on player's and computer's boards."""
        for ship_name, ship_size in SHIP_TYPES.items():
            player_ship = GameShip(ship_name, ship_size)
            computer_ship = GameShip(ship_name, ship_size)
            self.__player_board.place_ship(player_ship)
            self.__computer_board.place_ship(computer_ship)

    def __player_attack(self):
        """Prompt the player to enter the row and column to attack and process the attack."""
        while True:
            row = input("Enter row to attack: ")
            col = input("Enter column to attack: ")

            if row.isdigit() and col.isdigit():
                row = int(row)
                col = int(col)
                if self.__is_valid_attack(row, col):
                    break

            print("Invalid input! Enter valid row and column numbers.")

        self.__computer_board.receive_attack(row, col)

    def __computer_attack(self):
        """Let the computer choose a random row and column to attack and process the attack."""
        while True:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            if self.__is_valid_attack(row, col):
                break
        print(f"Computer attacks: ({row}, {col})")
        self.__player_board.receive_attack(row, col)

    def __is_valid_attack(self, row, col):
        """Check if the attack at the specified row and column is valid."""
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE \
            and self.__computer_board.board[row][col] not in ['O', 'X']

    def __print_game_result(self):
        """Print the result of the game - whether the player won or lost."""
        print("\nGame Over!")
        if self.__player_board.is_game_over():
            print("Gz! You won!")
        else:
            print("OH nooo way!! HOW DO YOU LOOSSEE???")


game = Game()
game.play()
