from array import *
import numpy as np

def board_setup():

    def get_value():
        '''
        Function to get the initial state of the board
        Args:
            None
        Returns:
            value: string of the board state
        '''

        value = input("Please enter the 16 letters that appear on your boggle board with spaces in between:\n")
        return value

    def one_to_two_array(grid):
        oneDArray = np.array(grid)
        twoDArray = oneDArray.reshape(4,4)

        return twoDArray

    def string_to_array(s):
        return s.split(" ")

    def get_board():
        return one_to_two_array(string_to_array(letters))

    def confirm_board():
        confirm = input("Does this look like your expected output?\n")

        if confirm.lower() in ['y', 'yes']:
            print(f'\nGreat!')
        elif confirm.lower() in ['n', 'no']:
            print(f'\nTry again!')
            board_setup()
        else:
            print(f'\nThere was an error with your input, try again! This time please respond with yes or no.')
            confirm_board()

    answer = get_value()

    letters = answer.strip().upper() # remove surrounding whitespace to make this more robust to user variation

    if len(string_to_array(letters))!=16:
        print(f'\nSomething was wrong with your input. Try again!')
        board_setup()
        exit()

    boggle_board = get_board()

    print(f'You entered {answer}, as a boggle board it looks like...\n{boggle_board}')

    confirm_board()

if __name__ == "__main__":
    board_setup()
