class Player:

    def __init__(self,name,words,num):
        self.name=name
        self.words=words
        self.num=num
        
    def Display_Details(self):
        print("\nPlayer\'s Name:",self.name)
        print("Player\'s List of Words:",self.words)
        print("Player Number:",self.num,"\n")

def get_list_of_players():
    list_of_player_names = []

    def reset_players_names():
        list_of_player_names = []

    def reset_num_of_players():
        total_num_players = int(input(f'How many total players are there?\n'))

    for x in range(0, total_num_players):
        n = input(f'\nPlease enter the name of player {x+1}:\n')
        w = input(f'Please enter this player\'s words with spaces in between each word:\n').split(" ")
        p = int(x + 1)
        
        player=Player(n,w,p)
        # player.Display_Details()
            
        list_of_player_names.insert(x, player.name)
    
    print("\nList of Players:", list_of_player_names)

    def confirmation():
        confirm = input("\nDoes this look like your expected output?\n")
        if confirm.lower() in ['y', 'yes']:
            print(f'\nGreat!')
            exit()
        elif confirm.lower() in ['n', 'no']:
            error = input(f'\nEnter 1 if the error has to do with the number of players and 2 if it has to do with the players\' names!')

            def reset_error():
                error = input(f'\nEnter 1 if the error has to do with the number of players and 2 if it has to do with the players\' names!')
            
            if error == 1:
                reset_num_of_players()
            elif error == 2:
                reset_players_names()
            else:
                reset_error()

        else:
            print(f'\nThere was an error with your input, try again! This time please respond with yes or no.')
            confirmation()
    
    confirmation()

total_num_players = int(input(f'How many total players are there?\n'))
get_list_of_players()


