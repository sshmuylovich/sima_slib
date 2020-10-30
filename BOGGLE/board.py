from array import *
import numpy as np

class Board():
    """
    Boggle Board
    """
    def __init__(self, letters):
        """
        Instantiate the board with a given string of letters and prompt the user with a confirmation until the board is set up.

        Args:
            letters (str): String of 16 letters, separated by spaces, to place on the boggle board
        """
        self.letters = letters

        list_of_letters = letters.strip().upper().split(" ")

        def reset():
            value = input("Please enter the 16 letters that appear on your boggle board with spaces in between:\n")
            board = Board(value)
        
        if len(list_of_letters) != 16:
            print(f'\nSomething was wrong with your input. Try again!')
            reset()
        else:
            grid = np.array(list_of_letters).reshape(4,4)
            print(f'\nYou entered {letters}, as a boggle board it looks like...\n{grid}\n')

        def confirmation():
            confirm = input("Does this look like your expected output?\n")
            if confirm.lower() in ['y', 'yes']:
                print(f'\nGreat!')
                exit()
            elif confirm.lower() in ['n', 'no']:
                print(f'\nTry again!')
                reset()
            else:
                print(f'\nThere was an error with your input, try again! This time please respond with yes or no.')
                confirmation()
        
        confirmation()

value = input("Please enter the 16 letters that appear on your boggle board with spaces in between:\n")
board = Board (value)
