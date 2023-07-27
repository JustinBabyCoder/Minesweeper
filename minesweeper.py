import random


class Minesweeper:

    def __init__(self, size, difficulty):
        self.size = size  # Establish the size of the minesweeper grid
        self.mine_symbol = 'B'  # Indicator for a mine
        self.mines_count = None  # Initialized mines_count which will later be used to store the number of mines
        self.difficulty = difficulty # Define game difficulty

        self.field = [[[] for i in range(size)] for i in range(size)]  # Create the playing field as a 2D list                                     

        self.unused_cells = []  # Cells positions without bombs, yet to be initialised
        self.mines_pos = self.__set_mines()  # Initialize mines on the field and store their positions 
        self.__open_cell()  # Fill the non-mine cells with numbers indicating neighboring mines

    def __set_mines(self):
        # Determines the number of mines based on the grid size and difficulty
        self.mines_count = self.size * self.difficulty
        mines_pos = []
        self.unused_cells = []
        
        # Populate the list of unused cells, at start all cells are unused
        for i in range(self.size):
            for j in range(self.size):
                self.unused_cells.append((i, j))

        # Select random cells as mines and place them on the field
        for i in range(self.mines_count):
            mine = random.choice(self.unused_cells)
            y, x = self.unused_cells.pop(self.unused_cells.index(mine))
            mines_pos.append((y, x))
            self.field[y][x] = self.mine_symbol

        # Return a sorted list of mine positions
        return sorted(mines_pos)  

    def __define_cell(self, y, x):
        # Counts the number of mines in the 8 cells surrounding the given cell
        cell_num = 0
        around_cell = [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x - 1),
                       (y, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]

        for i in around_cell:
            if i in self.mines_pos:
                cell_num += 1

        # Returns the number of mines surrounding the cell
        return cell_num 

    def __open_cell(self):
        # Opens all non-mine cells and defines the number of surrounding mines for them
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] != self.mine_symbol:  
                    cell = self.__define_cell(i, j)
                    self.field[i][j] = str(cell)

    def __draw_field(self):
        # Display the current state of the field when called
        for i in self.field:
            print(*i)
