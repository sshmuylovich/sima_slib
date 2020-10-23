from array import *
import numpy as np

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
