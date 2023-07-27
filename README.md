# Minesweeper
# ENG
This is a simple, console-based implementation of the classic Minesweeper game. It is achieved using Python. The game consists of 3 files:

**Minesweeper.py (File 1)**: This file is responsible for creating the Minesweeper field, placing mines and assigning numbers to the cells. Here's what it does:

- Sets up a grid of specified size, with a range limit of 10 to 20.
- Places mines on the grid, the number of which is based on the size of the grid as well as the difficulty level.
- Assigns numbers to each non-mine cell, representing how many neighboring cells contain mines.

**game.py (File 2)**: This file is where the main gameplay occurs. It contains class Game with several methods for different game operations like digging (uncovering a cell), putting flags, validating the win or lose conditions, and displaying the game grid.

- Retrieves the user's preferred field size and difficulty level for the game.
- Dynamically assigns flags corresponding to the number of mines.
- Monitors user input for navigating through the game grid, placing flags or uncovering cells.

**main.py (File 3)**: This is the initiation file. Here, an instance of the Game class from game.py is created and the `play()` method is called to start the game. It is the entrypoint for the entire game.

The visual representation of the game grid, player’s progress, and end game notifications are all managed and provided in the console.

## Setup Instructions:
To set up the game, follow these steps:
- Clone the repository: `git clone <repository_link>`
- Navigate to the directory containing the files: `cd Minesweeper`
- Run the entrypoint script: `python main.py`

Have fun playing Minesweeper from your console!

## Dependencies:
Make sure you have the 'keyboard' python package installed. If not, use `pip install keyboard` to install it.

## Contributing:
Contributions are welcome! Please fork the repository and make changes as you'd like. Pull requests are encouraged.

## License:
This project is licensed under the terms of the MIT license. 
