from array import *
import numpy as np

def play_game():

    def one_to_two_array(grid):
        oneDArray = np.array(grid)
        twoDArray = oneDArray.reshape(5,5)

        return twoDArray

    def string_to_array(s):
        return s.split(" ")


    value = input("Please enter a the 25 letters that appear on your boggle board with spaces in between:\n")
        
    letters = value.strip().upper() # remove surrounding whitespace to make this more robust to user variation

    grid = one_to_two_array(string_to_array(letters))

    print(f'You entered {value}, as a boggle board it looks like...\n{grid}')

    # confirm = input("Does this look correct to you? Yes or No\n")

    # if confirm.upper() == "YES":
    #     x = 2
    #     break
    # elif confirm.upper() == "NO":
    #     x = 0
    #     print(f'Reinput your letters please.')
    # else:
    #     x = 1
    #     print(f'There was an error, can you please confirm your board again?')
