# Connect Four

## Overview

This repository/project is an implementation of the Connect Four game in Python. The project includes classes and functions to set up and play Connect Four, as well as an AI player to compete against. The main components of the project are:

- **Board Class**: Creates and handles the board, board initialization, checker placement, and win checks.
- **Player Class**: Represents a player in the game, either a human or AI, and handles move logic.
- **Game Logic**: Contains the main game loop and move processing functions.
- **AI Player**: Implements an AI player with customizable strategies for making moves.

## Project Files

### `board_class.py`

Defines the `Board` class for managing the Connect Four board. Key methods include:

- `__init__(self, height, width)`: Initializes the board with specified dimensions.
- `add_checker(self, checker, col)`: Adds a checker to the specified column.
- `is_win_for(self, checker)`: Checks for a win condition for the specified checker.
- `reset(self)`: Resets the board to its initial state.

### `player_class.py`

Defines the `Player` class for human players and AI. Key methods include:

- `__init__(self, checker)`: Initializes the player with a checker and number of moves.
- `next_move(self, b)`: Prompts the player for a move.
- `opponent_checker(self)`: Returns the checker of the opponent.

### `game_logic.py`

Contains the main game logic for playing Connect Four between two players. Key functions include:

- `connect_four(p1, p2)`: Plays a game of Connect Four between two players.
- `process_move(p, b)`: Processes a move made by a player and updates the board.

### `ai_player.py`

Defines the `AIPlayer` class for an AI opponent. Key methods include:

- `__init__(self, checker, tiebreak, lookahead)`: Initializes the AI with checker type, tie-breaking strategy, and lookahead depth.
- `scores_for(self, b)`: Calculates scores for each column based on current board state and lookahead depth.
- `next_move(self, b)`: Chooses the next move based on scoring and tie-breaking strategy.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/matthewchiccino/Connect-Four.git

