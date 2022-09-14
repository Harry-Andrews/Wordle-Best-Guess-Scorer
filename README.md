# Wordle-Best-Guess-Scorer
This is a project I made to give a score to a given wordle guess combination 
First we had to gather the wordle data using get_data.py
This used webscraping to take all the possible wordle answers from an article
Then I found a file with every english word and selected only english words that had a length of 5
This list represents our list of valid guesses.

The guess_checker function takes in a guess word and an answer word and out puts a list of the form
[0, 2, 1, 2, 1] where 0 represents a green letter, 1 represents an orange letter and 2 represents a grey letter.

In the original idea for the project I wanted to see what the "best" 3 word combinations to guess were
However on reinspection, it turns out there are over 280 billion different combinations of 3 valid guesses.
So the project in theory works, it just takes an inhuman amount of time.

The new purpose of the project became "evaluate the score of a certain guess combination".
I always guess the same 3 words: SALET DUCKY PRION, using this program it turns out that the best order for these guesses is
SALET PRION DUCKY as SALET has the best (read: lowest) individual word score 
while SALET PRION has a better score than SALET DUCKY

The project can easily be modified to its original purpose, but its requires an insane amount of computation.
