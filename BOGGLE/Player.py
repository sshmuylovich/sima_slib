class Player:
    # Defining a parameterized constructor having arguments
    def __init__(self,name,words,num):
        self.name=name
        self.words=words
        self.num=num
        
    def Display_Details(self):
        print("\nPlayer\'s Name:",self.name)
        print("Player\'s List of Words:",self.words)
        print("Player Number:",self.num,"\n")

total_num_players = int(input(f'How many total players are there?\n'))
list_of_player_names = []

for x in range(0, total_num_players):
    n = input(f'\nPlease enter the name of player {x+1}:\n')
    w = input(f'Please enter this player\'s words with spaces in between each word:\n').split(" ")
    p = int(x + 1)
    # Here we create the object for call 
    # which calls the constructor
    player=Player(n,w,p)
    # calling the instance method 
    # using the object student
#    player.Display_Details()

    list_of_player_names.insert(x, player.name)

print("\nList of Players:", list_of_player_names)
