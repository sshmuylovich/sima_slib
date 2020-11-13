def random_board():
    '''
        Creates the dice which have letters on each side --> Array of length 6 per die
    '''
    self.cube_one = ["A","A","E","E","G","N"]
    self.cube_two = ["A","O","O","T","T","W"]
    self.cube_three = ["D","I","S","T","T","Y"]
    self.cube_four = ["E","I","O","S","S","T"]
    self.cube_five = ["A","B","B","J","O","O"]
    self.cube_six = ["C","I","M","O","T","U"]
    self.cube_seven = ["E","E","G","H","N","W"]
    self.cube_eight = ["E","L","R","T","T","Y"]
    self.cube_nine = ["A","C","H","O","P","S"]
    self.cube_ten = ["D","E","I","L","R","X"]
    self.cube_eleven = ["E","E","I","N","S","U"]
    self.cube_twelve = ["H","I","M","N","QU","U"]
    self.cube_thirteen = ["A","F","F","K","P","S"]
    self.cube_fourteen = ["D","E","L","R","V","Y"]
    self.cube_fifteen = ["E","H","R","T","V","W"]
    self.cube_sixteen = ["H","L","N","N","R","Z"]


    self.cubes=[self.cube_one, self.cube_two, self.cube_three, self.cube_four, self.cube_five, self.cube_six, self.cube_seven, self.cube_eight, 
    self.cube_nine, self.cube_ten, self.cube_eleven, self.cube_twelve, self.cube_thirteen, self.cube_fourteen, self.cube_fifteen, self.cube_sixteen]

    self.cubes_temp = []

    self.letters = []

    for x in range (0, 16):
        self.random_cube = random.choice(self.cubes)
        self.cubes_temp.append(self.random_cube)
        self.cubes.remove(self.random_cube)
        self.random_letter = random.choice(self.random_cube)
        self.letters.append(self.random_letter)