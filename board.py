from array import *
import numpy as np

value = input("Please enter a the letters that appear on your boggle board with spaces in between:\n")
    
letters = value.upper()

def string_to_array(s):
    return s.split(" ")

grid = string_to_array(letters)

print(f'You entered {value}, as a boggle board it looks like... {letters}')
print(f'{grid}')


def one_to_two_array():
    oneDArray = np.array(grid)
    twoDArray = oneDArray.reshape(5,5)

    return twoDArray[5][5]

print(f'{one_to_two_array()}')

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
