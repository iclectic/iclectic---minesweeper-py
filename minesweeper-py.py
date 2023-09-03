import random
import re

# Create a board object to represent the Minesweeper game
# This allows us to interact with the game through methods like "create a new board object," "dig here," or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # Keep track of game parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create the game board
        self.board = self.make_new_board()  # Plant the bombs
        self.assign_values_to_board()

        # Initialize a set to keep track of uncovered locations
        self.dug = set()  # If we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # Generate a new game board based on the dimensions and number of bombs
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # Plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue  # Bomb already planted at this location

            board[row][col] = '*'  # Plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # Assign numbers (0-8) to empty spaces based on the number of neighboring bombs
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue  # Skip if it's a bomb
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    # ...
    # (Other methods like get_num_neighboring_bombs, dig, and __str__ remain unchanged)
    # ...

# Play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: Create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: Show the user the board and ask for where they want to dig
    # Step 3a: If location is a bomb, show the game over message
    # Step 3b: If location is not a bomb, dig recursively until each square is next to a bomb
    # Step 4: Repeat steps 2 and 3a/b until there are no more places to dig (victory or game over)
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        safe = board.dig(row, col)
        if not safe:
            break  # Game over

    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        # Reveal the whole board
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()
