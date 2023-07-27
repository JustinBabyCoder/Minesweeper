import os
import keyboard
from minesweaper import Minesweeper


class Game:

    def __init__(self):
        os.system('cls')  # Clear the console

        # Get the size of the field and the difficulty level from the user
        self.size = int(input("\nEnter field size --> "))
        self.difficulty = int(input("\nEnter difficulty:\n(1)EASY\n(2)MEDIUM\n(3)HARD\n--> "))
        
        # Game loop condition
        self.main_loop = True

        # Win and lose condition variables
        self.win = False
        self.loose = False

        # Initialize the game with the specified size and difficulty
        self.minesweeper = Minesweeper(self.size, self.difficulty)
        
        # Start with number of flags equal to number of mines
        self.flags = self.minesweeper.mines_count

        # Build the initial obscured field layout
        self.field = [['#' for i in range(self.size)] for i in range(self.size)]

        # Initialize the marker and its position on the board
        self.marker_sign = '+'
        self.marker_y, self.marker_x = [self.size // 2] * 2
        self.prev_cell = self.field[self.marker_y][self.marker_x]
        self.field[self.marker_y][self.marker_x] = self.marker_sign

        # Draw the game field initially
        self.draw()

    def dig(self):
        # Uncover and display cell content when the player digs
        x, y = self.marker_x, self.marker_y
        self.field[y][x] = self.minesweeper.field[y][x]
        if self.prev_cell == self.minesweeper.mine_symbol:
            pass

    def play(self):
        # Main game loop
        while self.main_loop:
            def on_press(key):
                # On key press, update the game state depending on the key pressed
                self.field[self.marker_y][self.marker_x] = self.prev_cell
                match key.name:
                    case "up":
                        if self.marker_y != 0:
                        self.marker_y -= 1  # Handle the marker moving up
                    case "down":
                        if self.marker_y != self.size - 1:
                        self.marker_y += 1  # Handle the marker moving down
                    case "left":
                        if self.marker_x != 0:
                        self.marker_x -= 1  # Handle the marker moving left
                    case "right":
                        if self.marker_x != self.size - 1:
                        self.marker_x += 1  # Handle the marker moving right
                    case "f": 
                        print('F')  # Handle flag placing, not ready
                    case "space": 
                        self.dig()  # Handle digging

                # Update the marker's position
                self.prev_cell = self.field[self.marker_y][self.marker_x]
                self.field[self.marker_y][self.marker_x] = self.marker_sign
                
                # Refresh the console and redraw the game field
                os.system('cls')
                self.draw()

            # Wait for a key press event
            keyboard.on_press(on_press)
            keyboard.wait()

    def draw(self):
        # Function to draw the game field
        game_name = 'MINESWEEPER'
        shift = (self.size * 2 - 2 - len(game_name)) // 2
        
        print(' ' * shift + game_name + '\n')  # Print the game name at the top
        
        def default():
            return self.field[i]

        # Print the game field with additional information
        for i in range(len(self.field)):
            match i:
                case 0:
                    print(*default(), '  ' + f'CURRENT CELL: {self.prev_cell}')  # Print the content of current cell
                case 1:
                    print(*default(), '  ' + f'FLAGS LEFT: {self.flags}')  # Print the remaining flags
                case _:
                    print(*default())  # Print the rest of the field
