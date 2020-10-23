from array import *
import numpy as np

num_player = 1

def test():
    global num_player
    num_player += 1

class Player:
    def __init__(self, name, words, num):
        self.name = name
        self.words = words
        self.num = num

    def Display_Details(self):
        print("Player Number: ",self.num)
        print("Player Name: ",self.name)
        print("Player words: ",self.words)

    list_of_players = list()

    def players():
        total_num_players = int(input(f'How many total players are there?\n'))

        for x in range(0, total_num_players):
            test()
            player = Player(input(f'Please enter the name of player {num_player}:\n'), 
            input(f'Please enter this player\'s words with spaces in between each word:\n').split(" "), 
            num_player)
            list.append(player)

def get_players_names():
    '''
    Function to get player names from use input
    Args:
        None
    Returns:
        names: string containing player names
    '''
    value = input("Please enter the name of each players with spaces in between names:\n")

    names = value.strip().upper()
    return names

def setup_players_scores():
    '''
    Function to initialize player scores to zero and print the scores
    Args:
        None
    Returns:
        None
    '''
    def string_to_array(s):
        return s.split(" ")

    list_of_names = string_to_array(get_players_names())
    num_players = len(list_of_names)

    scorecard = np.zeros(num_players)

    print(f'List of players:{list_of_names}\nand their current scores:{scorecard}')
    confirm_players()

def confirm_players():
        confirm = input("\nDoes this look like your expected output?\n")

        if confirm.lower() in ['y', 'yes']:
            print(f'\nGreat!')
        elif confirm.lower() in ['n', 'no']:
            print(f'\nTry again!')
            setup_players_scores()
        else:
            print(f'\nThere was an error with your input, try again! This time please respond with yes or no.')
            confirm_players()


if __name__ == "__main__":
    setup_players_scores()
