# sima_boggle
## Function:
For a round of Boggle: to check the validity of each player's words, score their respective lists, and declare a winner. 

__Thoughts behind how I'm going to get this to work:__

After a game of Boggle, the user will:
- input the letters used in the round of boggle from left to right, top to bottom
- input the number of players that round

The program will then prompt each user to input their words in a comma separated list. The program will compare each word of a player to the other players' lists. If the word belongs to more than half of the players, it gets removed from all lists containing the word. If not, the word is searched for in the Merriam Webster Dictionary. If that word exists, the points gained from that word (based on the word's length) are added to each player that has that word to their respective total score. 

[Rules of Boogle](https://www.fgbradleys.com/rules/Boggle.pdf)

## Requirements
 - For Wondows, MacOS, and Linux OTF: 
  - Go to [Open Dyslexic's Content](https://gumroad.com/d/b958739359e5e36637620f47268d2c87) 
  - Download OpenDyslexic Mono
 - For iOS and Android
  - Go to [Open Dyslexic's Content](https://gumroad.com/d/b958739359e5e36637620f47268d2c87)
  - Download the compatible OpenDyslexic Font zip file 
  - Open [boggle_gui.py](https://github.com/sshmuylovich/sima_boggle/blob/main/BOGGLE/GUI/boggle_gui.py)
  - Change the 'family' value in the following method to the corresponding name in your device's font menu
   ```python
   def set_font_open_dyslexic_cubes(self):
      font = "%(family)s %(size)i %(weight)s %(slant)s" % {'family': 'OpenDyslexicMono', 'size': 70, 
      'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
      self.configure(font=font)
   ```

## Completed Features:
## Features in Progress:
- boggle_board.py
- player.py
- check_words_dictionary.py
- score.py
- family_score.py
- boggle_gui.py
## Future Features:
- check_words_board
- check_words_players
- final_results
## Questions & Recommended Help:
- Continue developping [boggle_git.py](https://github.com/sshmuylovich/sima_boggle/blob/main/BOGGLE/boggle_gui.py).
- How do I search the Merriam Webster Dictionary for the word? How do I rule out all informal or archaic words?
  - A potential option: use [this](https://github.com/pfeyz/merriam-webster-api) Python wrapper of the Merrian Webster API. You need to get developer keys from [here](https://www.dictionaryapi.com/) and then take a look at [this](https://github.com/pfeyz/merriam-webster-api/blob/master/examples/define.py) script, which fetches the definition for a given query (or will return `No definitions found for 'word'`). 


## Citations

[OpenDyslexic](https://opendyslexic.org/) is a new open sourced font created to increase readability for readers with dyslexia. While not perfect, its typeface was designed with the intention of combating some of the most common symptoms of dyslexia.
