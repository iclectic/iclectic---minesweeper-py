# Minesweeper Game in Python

![Minesweeper](minesweeper.png)

This Python program implements the classic Minesweeper game. It allows you to play the game in the console, revealing tiles and avoiding hidden mines. The program uses object-oriented programming principles to create and manage the game board.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Game Controls](#game-controls)
- [Author](#author)
- [License](#license)

## Features

- A console-based Minesweeper game.
- Customizable game board dimensions and the number of mines.
- Safe and user-friendly input handling.
- A clear game-over message and a victory message.
- Clean and organized Python code.

## Getting Started

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/yourusername/minesweeper.git

Navigate to the project directory:

```cd minesweeper

2. ```Run the Minesweeper game:

python minesweeper.py


## How to Play
- The game board is displayed in the console. Empty tiles are represented by numbers, indicating the number of adjacent mines.
- To start playing, enter the row and column where you want to dig. For example, entering "0,3" will dig at row 0, column 3.
- Keep digging and uncovering tiles while avoiding mines. The game continues until you either clear the entire board or dig on a mine.

## Game Controls
- Use the format row,col to specify your dig location (e.g., "0,3").
- Invalid inputs or out-of-bounds selections will result in a prompt to try again.
- The game ends when you either clear the board (victory) or dig on a mine (game over).
