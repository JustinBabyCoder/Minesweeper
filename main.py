# Import the Game class from the game module
from game import Game

# The "__name__" is a built-in variable in Python, which is the name of the current module.
# If the module is being run directly (not being imported), "__name__" is set to "__main__".
if __name__ == '__main__':
    game = Game()  # Instantiate the Game class
    game.play()  # Call the play method from the Game instance to start the game
