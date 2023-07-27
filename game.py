import os
import time
import keyboard
from minesweeper import Minesweeper

# This is the main game class
class Game:

    # Constructor method to initialize the game
    def __init__(self):
        # Clear console for a clean start
        os.system('cls')  

        # Get preferred field size and difficulty from user
        self.size = int(input("\nEnter field size --> "))
        self.difficulty = int(input("\nEnter difficulty:\n(1)EASY\n(2)MEDIUM\n(3)HARD\n--> "))

        # Main game loop condition
        self.main_loop = True

        # Initiate game with user's size and difficulty prefs
        self.minesweeper = Minesweeper(self.size, self.difficulty)
        
        # Initial game state setup
        self.flag_sign = 'F'
        self.flags = self.minesweeper.mines_count
        self.current_flags = {}
        self.field = [['#' for i in range(self.size)] for i in range(self.size)]
        self.win_field = [[j if j != self.minesweeper.mine_symbol else self.flag_sign for j in i] for i in self.minesweeper.field]
        self.win = False
        self.loose = False
        self.marker_sign = '+'
        self.marker_y, self.marker_x = [self.size // 2] * 2
        self.prev_cell = self.field[self.marker_y][self.marker_x]
        self.field[self.marker_y][self.marker_x] = self.marker_sign

        os.system('cls')
        # Draw initial game field
        self.draw()

    # Method to handle digging - uncovering a cell
    def dig(self):
        x, y = self.marker_x, self.marker_y
        self.field[y][x] = self.minesweeper.field[y][x]
        if self.prev_cell == self.flag_sign:
            self.flags += 1
        self.win_lose_check()

    # Method to manage flag placement/removal
    def put_flag(self):
        x, y = self.marker_x, self.marker_y

        if (y, x) not in self.current_flags and self.flags > 0:
            self.current_flags[(y, x)] = self.field[y][x]
            self.field[y][x] = self.flag_sign
            self.flags -= 1
        else:
            if self.field[y][x] == self.flag_sign:
                self.field[y][x] = self.current_flags[(y, x)]
                del self.current_flags[(y, x)]
                self.flags += 1
        self.win_lose_check()
 
    # Method to verify if game is over (win or loose)
    def win_lose_check(self):
        if self.field[self.marker_y][self.marker_x] == self.minesweeper.mine_symbol:
            self.loose = True
            self.main_loop = False

        if self.field == self.win_field:
            self.win = True
            self.main_loop = False


    # Handle key press functionality & update game state accordingly
    def play(self):
        def on_press(key):
            self.field[self.marker_y][self.marker_x] = self.prev_cell

            # Manage player's movement and actions
            match key.name:
                case "up":
                    if self.marker_y != 0:
                        self.marker_y -= 1  
                case "down":
                    if self.marker_y != self.size - 1:
                        self.marker_y += 1  
                case "left":
                    if self.marker_x != 0:
                        self.marker_x -= 1  
                case "right":
                    if self.marker_x != self.size - 1:
                        self.marker_x += 1  
                case "f":
                    self.put_flag()
                case "space":
                    self.dig()

            # Update marker's position
            self.prev_cell = self.field[self.marker_y][self.marker_x]
            self.field[self.marker_y][self.marker_x] = self.marker_sign

            # Refresh console and redraw field after each action
            os.system('cls')
            self.draw()

        keyboard.on_press(on_press)
        while self.main_loop:
            time.sleep(1)

    # Method to draw the game field on console
    def draw(self):
        game_name = 'MINESWEEPER'
        shift = (self.size * 2 + 2 - len(game_name)) // 2
        
        print(' ' * shift + game_name + '\n')  

        vertical = lambda: ''.join(['|'] + self.field[i] + ['|'])
        horizontal = lambda: ''.join(['—' for i in range(self.size + 2)])

        print(*horizontal())
        for i in range(len(self.field)):
            match i:
                case 0:
                    print(*vertical(), '  ' + f'CURRENT CELL: {self.prev_cell}')  # Indicate the content of the current cell
                case 1:
                    print(*vertical(), '  ' + f'FLAGS LEFT: {self.flags}')  # Display the number of flags left
                case 3:
                    # Display game ending messages
                    if self.loose:
                        print(*vertical(), '  ' + f'YOU LOSE!')
                    elif self.win:
                        print(*vertical(), '  ' + f'YOU WON!')
                    else:
                        print(*vertical())  # Continue the game if game didn't end yet
                case _:
                    print(*vertical())  # Layout of the rest of the field
        print(*horizontal())  # Construct the horizontal borders
