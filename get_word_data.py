import pickle
import requests
from bs4 import BeautifulSoup, element

URL = "https://medium.com/@owenyin/here-lies-wordle-2021-2027-full-answer-list-52017ee99e86"
response = requests.get(URL)
wordle_answers_webpage = response.text

soup = BeautifulSoup(wordle_answers_webpage, "html.parser")

big_text = soup.find(id="1d6d") #This just happened to be the id of where all of the words were stored (check web link!)
answer_list = []

for x in big_text:
    if type(x) == element.NavigableString and "*" not in x:
        #6 words were removed and so end in an asterisk - we dont want these words in the list hence the above.
        word_to_be_added = x[-5:None] #TIL that None represents the index after -1, so this returns all 5 letters that we want
        answer_list.append(word_to_be_added)

answer_list.remove(" DONT") #The word for day 560 is DONT REPOST - The writer's sense of humor almost broke my code!

with open("answer_list.pkl", "wb") as f:
    pickle.dump(answer_list, f)

with open("wordle_answers.txt", "w") as f:
    for answer in answer_list:
        f.write(answer + "\n")

# The data is stored in a text file AND a pickle file (just for practice)

# The code below this generates all our valid guesses which are taken from a text file I copy-pasted from the internet.
# The word list was taken from https://scipython.com/static/media/uploads/blog/wordle/sowpods

valid_guesses = []

with open("every_english_word.txt", "r") as f:
    number_of_lines = 267753
    while number_of_lines > 0:
        number_of_lines -= 1
        word_to_be_added = f.readline().strip()
        if len(word_to_be_added) == 5:
            valid_guesses.append(word_to_be_added)

with open("valid_guesses.pkl", "wb") as f:
    pickle.dump(valid_guesses, f)
