# Minesweeper Game - README

This repository contains a Python implementation of the classic Minesweeper game, playable on the console.

The game allows users to designate the size of the field and the difficulty of the game.

## Files Description:

- `main.py`: This is the entry file for starting the game.

- `minesweeper.py`: This contains the `Minesweeper` class, which initiates and configures the game field and mines.

- `gamy.py`: This contains the `Game` class that handles the game logic, player actions and controls the gameplay.

- `colors.py`: This contains the `ColorMinesweeper` class, which handles the coloring of the symbols on the game field. It uses the `colorama` module for this purpose.

## How to play:

To start the game, run the `file1.py`. It will ask for the field size and the difficulty level you desire. 

You can use the arrow keys to move the marker based on the direction pressed. Press the `f` key to flag a cell. You can unflag a cell by pressing `f` on a cell that has already been flagged. Press the `space` key to dig a cell.

Flag counts and current cell status will be displayed on the console during the game.

If you dig a cell that contains a mine, the game is over and you lose. If you manage to flag all the mines without digging on any, you win!

## Modules Used:

Python's `os`, `time`, `keyboard`, `random` and `colorama` modules are used in this project.

## Note: 

- This game requires the `keyboard` and `colorama` modules which are not part of Python's standard library. You can easily install these with pip using the command `pip install keyboard colorama`.

- Be aware that the `keyboard` module may require root access to function properly.

Enjoy the game! 
