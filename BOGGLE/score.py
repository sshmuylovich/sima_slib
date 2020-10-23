from urllib.request import urlopen, Request
from urllib.error import HTTPError
from wordster import wordster
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

# def check_word_recurse (word, time_bound):
#     '''
#     A method that returns True if the word is a real word and False otherwise.

#     Note that if there are too many requests (HTTP Error 429), it will try again
#     over and over.  Call check_word and not this because this might potentially
#     take forever.

#     Args:
#         word: the word to be tested.
#         time_bound: the deadline for calculating this word.

#     Returns:
#         boolean: whether the word is a real word.
#     '''
    
#     if time.time() > time_bound:
#         raise Exception("Took too long to process request")
#     try:
#         html = urlopen(Request("https://api.dictionaryapi.dev/api/v2/entries/en/" + word, headers={'User-Agent': 'Mozilla'}))
#     except HTTPError as err:
#         if str(err.code) == "404": # The case where the word is not found.
#             return False
#         elif str(err.code) == "429": # Too many requests: wait 5 seconds, and try again.
#             time.sleep(5)
#             return check_word_recurse(word, time_bound)
#         else:
#             raise
#     text = html.read().decode("utf-8")
#     # Check that the word returned is actually the word inputted.
#     # Prevents errors like "ix" is a word because "ix" is Roman numerals for 9.
#     lines = text.split()
#     new_word = lines[3][1:-2]
#     if new_word != word:
#         return False
#     else:
#         return True

# def check_word (word, time_limit=15.0):
#     '''
#     A method that returns True if the word is a real word and False otherwise,
#     with a time limit built in in case it takes too long.  Note that the time
#     taken could exceed time_limit slightly, but it shouldn't be too significant.

#     Args:
#         word: the word to be tested.
#         time_limit: the maximum time, in seconds, that the operation can take.

#     Returns:
#         boolean: whether the word is a real word.
#     '''

#     return check_word_recurse(word, time.time() + time_limit)

if __name__ == "__main__":
#    check_word("hello")
    print(f'{wordster.find_meaning("jargon")}')