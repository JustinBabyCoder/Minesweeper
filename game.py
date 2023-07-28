import os
import time
import keyboard
import random
from colors import ColorMinesweeper
from minesweeper import Minesweeper

# Class that handles the game logic 
class Game:

    # Initialize the game with a user-determined size and difficulty level
    def __init__(self):  
        os.system('cls')  # clear the terminal 

        # Request field size and difficulty from the user
        self.size = int(input("\nEnter field size --> "))
        self.difficulty = int(input("\nEnter difficulty:\n(1)EASY\n(2)MEDIUM\n(3)HARD\n--> "))

        self.main_loop = True  # condition for the main game loop

        # Initializing game parameters with the user's inputs
        self.minesweeper = Minesweeper(self.size, self.difficulty)
        self.colors = ColorMinesweeper() 
        
        # Set gameplay parameters
        self.flag_sign = 'F'  # flag representation
        self.flags = self.minesweeper.mines_count  # number of flags, which equals number of mines
        self.current_flags = {}  # dictionary to store the current flags

        # Initialize the game field as a 2D list filled with '#'
        self.field = [['#' for i in range(self.size)] for i in range(self.size)]

        # Construct the winning field, replacing every mine symbol with a flag sign in the minesweeper's field
        self.win_field = [[j if j != self.minesweeper.mine_symbol else self.flag_sign for j in i] for i in self.minesweeper.field]
        self.win = False  # game win status
        self.loose = False  # game lose status
        self.marker_sign = '+'  # marker to show the current selected cell

        # Initialize marker position to the random empty position
        self.marker_y, self.marker_x = self.__start_position()

        # Store the current cell's content
        self.prev_cell = self.field[self.marker_y][self.marker_x]

        # Mark the current cell's position on the game field
        self.field[self.marker_y][self.marker_x] = self.marker_sign

        os.system('cls')  # clear the terminal 
        self.draw()  # draw the initial game field

    # Methon to set start marker's position
    def __start_position(self):
        empty_cells = []
        for i in self.minesweeper.unused_cells:
            y, x = i
            if self.minesweeper.field[y][x] == ' ':
                empty_cells.append((y, x))
        return random.choice(empty_cells)

    # Uncover a cell and apply game rules
    def dig(self):
        x, y = self.marker_x, self.marker_y  # get current marker position

        # Replace the current revealed cell sign with the corresponding cell from the minesweeper field
        self.field[y][x] = self.minesweeper.field[y][x] 

        # List of tuples to check neighboring cells (up, down, left, and right)
        around = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x - 1),
                    (y, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]
        # Loop to check each neighbor of the currently revealed cell
        for i in around:
            y1, x1 = i
            # Checking if a neighbor's coordinate is out of boundaries - if yes, replace it with the current cell's position
            if y1 >= self.size or y1 < 0 : y1 = y
            if x1 >= self.size or x1 < 0 : x1 = x
            # If the neighbor's cell is not a flag, reveal its content from the minesweeper field
            if self.field[y1][x1] != self.flag_sign:
                self.field[y1][x1] = self.minesweeper.field[y1][x1]
            # If the neighbor's cell is a mine, end the game with a loss
            if self.field[y1][x1] == self.minesweeper.mine_symbol:
                self.main_loop = False
                self.loose = True

        # If the previous cell was a flag, increment the available flags count by one
        if self.prev_cell == self.flag_sign:
            self.flags += 1
        # Check game status each time a cell is revealed
        self.game_over_check() 

    # Method to manage flag placements 
    def put_flag(self):
        x, y = self.marker_x, self.marker_y  # get current marker position

        # Check conditions to place or remove a flag
        # If current cell is not flagged, user has remaining flags, and cell is not revealed:
        # Place a flag and decrease the flags count by one
        if (y, x) not in self.current_flags and self.flags > 0 and self.field[y][x] != ' ':
            self.current_flags[(y, x)] = self.field[y][x]
            self.field[y][x] = self.flag_sign
            self.flags -= 1
        else:
            # If the cell is flagged: remove flag, restore the original cell content, and increase flags count by one
            if self.field[y][x] == self.flag_sign:
                self.field[y][x] = self.current_flags[(y, x)]
                del self.current_flags[(y, x)]
                self.flags += 1
        # Check game status each time a flag is placed or removed
        self.game_over_check() 

    # Check if the game is over 
    def game_over_check(self):
        # If the current cell is a mine, the game ends with loss
        if self.field[self.marker_y][self.marker_x] == self.minesweeper.mine_symbol:
            self.loose = True  # Loss status set to True
            self.main_loop = False  # Stop the main loop

        # If the current game field equals the winning field, player wins
        if self.field == self.win_field:
            self.win = True  # Win status set to True
            self.main_loop = False  # Stop the main loop

    # The main function that handles player actions in the game
    def play(self):

        # Function to manage key press actions 
        def on_press(key):
            # Update the state of the current cell in the game field
            self.field[self.marker_y][self.marker_x] = self.prev_cell
            
            # Manage player's movement and actions 
            match key.name:
                # Move marker up if not at the top boundary
                case "up":
                    if self.marker_y != 0:
                        self.marker_y -= 1  
                # Move marker down if not at the bottom boundary
                case "down":
                    if self.marker_y != self.size - 1:
                        self.marker_y += 1
                # Move marker left if not at the left boundary
                case "left":
                    if self.marker_x != 0:
                        self.marker_x -= 1
                # Move marker right if not at the right boundary
                case "right":
                    if self.marker_x != self.size - 1:
                        self.marker_x += 1  
                # Put a flag if 'f' key is pressed
                case "f":
                    self.put_flag()
                # Dig in a cell if 'space' key is pressed
                case "space":
                    self.dig()

            # Update position of the marker
            self.prev_cell = self.field[self.marker_y][self.marker_x]
            self.field[self.marker_y][self.marker_x] = self.marker_sign

            # Refresh console and redraw the field after each action
            os.system('cls')
            self.draw()

        # Register the key press handler function
        keyboard.on_press(on_press)

        # Keep running the game while main_loop is True
        while self.main_loop:
            time.sleep(1)

    # Method to draw the game field in the console
    def draw(self):
        game_name = 'MINESWEEPER (by JustinBabyC0der)'  

        # Function to return a string of vertical game field borders
        vertical = lambda: '|' + ''.join([self.colors.to_color(i) for i in self.field[i]]) + '|'
        
        # Function to construct the horizontal borders of the game field
        horizontal = lambda: ''.join(['—' for i in range(self.size + 2)])

        # Print the top border
        print(horizontal())
        
        # Print each row of the game field
        for i in range(len(self.field)):
            match i:
                # Indicate the content of the current cell
                case 0:
                    print(vertical(), '  ' + game_name)
                case 2:
                    print(vertical(), '  ' + f'CURRENT CELL: {self.prev_cell}')
                # Display the number of flags left
                case 3:
                    print(vertical(), '  ' + f'FLAGS LEFT: {self.flags}')
                case 5:
                    # Display game ending messages
                    if self.loose:
                        print(vertical(), '  ' + f'YOU LOSE!')
                    elif self.win:
                        print(vertical(), '  ' + f'YOU WON!')
                    else:
                        # Continue the game if it is not over yet
                        print(vertical())
                case _:
                    # Print the rest of the game field
                    print(vertical())
        # Print the bottom border
        print(horizontal())
