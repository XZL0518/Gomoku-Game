# Gomoku-Game
1. Requirements
   
Python 3.x

Uses only standard libraries: random, time

2. Installation & Execution
   
Place all script files (create_board.py, game.py) in the same directory.

Open a terminal and navigate (cd) to that directory.

Run the game using:

python game.py

The game starts with an empty 15x15 board. You play as 'X', and the AI plays as 'O'.

3. Game Rules & Controls

The board is a 15x15 grid.

Players alternate placing their marks ('X' for you, 'O' for AI) on empty cells (denoted by '.').

To place a mark, input coordinates as two numbers separated by space, e.g. 3 4 means column 3, row 4. Coordinates range from 1 to 15.

The goal is to get 5 consecutive marks in a row, column, or diagonal.

If the map is full of marks, no ones wins.

The AI uses simple strategies:

Put the first 'O' on random cell in the whole map.

First block four in a row if they were arranged in order.

Then block three in a row if they were arranged in order.

(If the player does not extend a blocked three-mark line into four, the AI will temporarily not block it.)

Otherwise, place marks near its existing 'O's or random empty spots.

4. Features

The game displays the board after every move with row and column numbers.

Input validation checks for valid coordinates and occupancy.

Detects and announces win or draw (board full).

AI automatically plays after your move.

Currently, the AI strategy is non-aggressive and algorithms can be further optimized to enhance the game's challenge and engagement.

6. Code Structure

create_board.py: contains board creation, display, and AI logic.

game.py: handles game loop and user input.

