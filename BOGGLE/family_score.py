from urllib.request import urlopen, Request
from urllib.error import HTTPError
import time
# Why do I have these imports?

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
    elif len(word) == 3:
        return 1
    elif len(word) > 3:
        return len - 3
    else:
        return NotImplementedError

# if __name__ == "__main__":