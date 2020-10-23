from urllib.request import urlopen, Request
from urllib.error import HTTPError
import time

def score_word(word):
    '''
    Function to score a given Boggle word
    Args:
        word: string of the given Boggle word
    Returns:
        score: int score
    '''

    if len(word) < 3:
        return 0
    elif len(word) in [3,4]:
        return 1
    elif len(word) == 5:
        return 2
    elif len(word) == 6:
        return 3
    elif len(word) == 7:
        return 4
    elif len(word) >= 8:
        return 11
    else:
        return NotImplementedError

# if __name__ == "__main__":