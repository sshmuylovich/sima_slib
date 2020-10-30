from array import *
import numpy as np

class Board():
    def __init__(self, letters):
        self.letters = letters
        list_of_letters = letters.strip().upper().split(" ")

        # TODO This is just a flag with a higher scope so I can end the recursive search - someone should find a better way
        self.is_word_found = False

        def reset():
            value = input("Please enter the 16 letters that appear on your boggle board with spaces in between:\n")
            board = Board(value)

        if len(list_of_letters)!=16:
            print(f'\nSomething was wrong with your input. Try again!')
            reset()
        else:
            self.grid = np.array(list_of_letters).reshape(4,4)
            print(f'\nYou entered {letters}, as a boggle board it looks like...\n{self.grid}\n')

        def confirmation():
            confirm = input("Does this look like your expected output?\n")
            if confirm.lower() in ['y', 'yes']:
                print(f'\nGreat!')
                return
            elif confirm.lower() in ['n', 'no']:
                print(f'\nTry again!')
                reset()
            else:
                print(f'\nThere was an error with your input, try again! This time please respond with yes or no.')
                confirmation()

        confirmation()

    def _check_word_board_pos(self, word, row, col, is_searched=[], num_letters=0):
        '''
        Recursive helper function for check_words_board that checks if the word can be created from position (row, col)
        Args:
            word (str): the word to check for
            row: row index to start from
            col: col index to start from
            is_searched: list containing positions we've searched
            num_letters: which letter index we are on for this word

        Returns:
            None; changes the value of the attribute self.is_word_found to True if the word is found
            # TODO this is really really bad but I don't remember how to properly pop true from the recursion stack oops
            If someone feels like it make this actually return True instead of just changing the attribute
        '''
        word = word.upper()
        word_len = len(word)

        letter = self.grid[row][col]
        is_searched.append((row, col))

        # This path contains the wrong letter for the current position
        if letter != word[num_letters]:
            print('wrong letter')
            pass

        # If for the whole length of the word all of the letters have been the same, then the word has been found
        elif num_letters == word_len-1:
            self.is_word_found = True
            print('word is found!')
            return

        # If none of these is the case, we need to keep searching
        else:
            # potential moves are in all eight directions
            potential_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            valid_new_positions = []
            for r, c in potential_moves:
                next_row = row + r
                next_col = col + c

                # If the move is within the grid, the move goes to a position not previously searched, and the word isn't found, call the recursive function

                #print(is_searched)
                #print(self.is_word_found)

                if 0 <= next_row < 4 and 0 <= next_col < 4 and (next_row, next_col) not in is_searched and not self.is_word_found:
                    self._check_word_board_pos(word, next_row, next_col, is_searched.copy(), num_letters+1)

    def check_words_board(self, word):
        '''
        Checks to see if word is in the board via depth-first-search.

        Args:
            word (str): the word to check for

        Returns:
            is_found (bool): whether the word is within the board
        '''
        word_len = len(word)

        # loop through all potential starting positions
        for row in range(4):
            for col in range(4):
                if self.is_word_found:
                    # reset this for the next word to check
                    self.is_word_found = False
                    return True

                # check whether the word exists at the current starting position
                #print((row, col))
                self._check_word_board_pos(word, row, col, is_searched=[])

        # we've checked all starting grid positions and no word, so it isn't in the board
        return False




value = input("Please enter the 16 letters that appear on your boggle board with spaces in between:\n")
board = Board(value)
