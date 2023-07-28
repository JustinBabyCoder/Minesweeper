from colorama import Fore, Back, Style, init

class ColorMinesweeper:

    def __init__(self):
        init(autoreset=True)

        self.symbol_colors = {
            '+': (Fore.BLACK, Back.WHITE),
            '#': (Fore.BLACK, Back.BLACK),
            'B': (Fore.YELLOW, Back.RED),
            'F': (Fore.RED, Back.YELLOW),
            ' ': (Fore.WHITE, Back.WHITE),
            '1': (Fore.BLUE, Back.BLACK),
            '2': (Fore.GREEN, Back.BLACK),
            '3': (Fore.RED, Back.BLACK),
            '4': (Fore.BLUE, Back.BLACK),
            '5': (Fore.RED, Back.BLACK),
            '6': (Fore.CYAN, Back.BLACK),
            '7': (Fore.YELLOW, Back.BLACK),
            '8': (Fore.MAGENTA, Back.BLACK),
        }

    def to_color(self, symbol):
        color_set = self.symbol_colors[symbol]
        # Removed str() from the return line
        return color_set[0] + color_set[1] + symbol + Style.RESET_ALL
