# Import the Game class from the game module
from game import Game

# The "__name__" is a built-in variable in Python, which is the name of the current module.
# If the module is being run directly (not being imported), "__name__" is set to "__main__".
if __name__ == '__main__':
    game = Game()  # Instantiate the Game class
    game.play()  # Call the play method from the Game instance to start the game






#                   Обязательно!!!
# Сделать все по стандартам ООП
# Постараться все разбить на классы
# Вывести стартовое меню в отдельный класс
# Избавиться от повторений, match case и if при помощи dict
# Вынести общие настройки в отдельный файл с общ. доступом
# Переформатировать метод dig() класса Game
# Пересмотреть подход к методу game_over_check() класса Game
# Добавить возможность открывать одну ячейку
# Сделать маркер динамичным, т.е. будет изменять цвет prev_cell
# Добавить время
# Добавить возможность вести статистику, где будет время
#   ...прохождения, конфигурация поля

#                   ПО ВОЗМОЖНОСТИ!!!
# Поиграться с дизайном для названия игры
# Изменить стартовое меню (в плане дизайна)
# Попробовать сделать игру исполняемым файлом .exe
# Добавить инструкцию к игре в стартовом меню при помощи команды
# Ввести систему очков