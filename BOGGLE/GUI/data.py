import random 

letters = []

def get_letter(i):
    return letters[i]

def set_letter(i, text):
    return letters.insert(i, text)

def clear_letters():
    letters.clear()

def check_letters():
    for i in letters:
        if len(i) != 1:
            if i.__eq__("QU"):
                pass
            else:
                return False
        if i.isalpha() == False:
            return False
        
    return True

def random_values():
    '''
        Creates the dice which have letters on each side --> Array of length 6 per die
    '''
    cube_one = ["A","A","E","E","G","N"]
    cube_two = ["A","O","O","T","T","W"]
    cube_three = ["D","I","S","T","T","Y"]
    cube_four = ["E","I","O","S","S","T"]
    cube_five = ["A","B","B","J","O","O"]
    cube_six = ["C","I","M","O","T","U"]
    cube_seven = ["E","E","G","H","N","W"]
    cube_eight = ["E","L","R","T","T","Y"]
    cube_nine = ["A","C","H","O","P","S"]
    cube_ten = ["D","E","I","L","R","X"]
    cube_eleven = ["E","E","I","N","S","U"]
    cube_twelve = ["H","I","M","N","QU","U"]
    cube_thirteen = ["A","F","F","K","P","S"]
    cube_fourteen = ["D","E","L","R","V","Y"]
    cube_fifteen = ["E","H","R","T","V","W"]
    cube_sixteen = ["H","L","N","N","R","Z"]


    cubes=[cube_one, cube_two, cube_three, cube_four, cube_five, cube_six, cube_seven, cube_eight, 
        cube_nine, cube_ten, cube_eleven, cube_twelve, cube_thirteen, cube_fourteen, cube_fifteen, cube_sixteen]

    cubes_temp = []


    for x in range (0, 16):
        random_cube = random.choice(cubes)
        cubes_temp.append(random_cube)
        cubes.remove(random_cube)
        random_letter = random.choice(random_cube)
        letters.append(random_letter)