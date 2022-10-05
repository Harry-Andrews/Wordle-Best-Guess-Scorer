import time
from guess_checker import check_guess
import pickle

with open("valid_guesses.pkl", "rb") as f:
    valid_guesses = pickle.load(f)

with open("answer_list.pkl", "rb") as f:
    answer_list = pickle.load(f)
#### This section takes the input guesses that you would like to score
valid_input = False

while not valid_input:
    try:
        number_of_words = int(input("How many starting Wordle guesses would you like to score? "))
    except:
        print("Invalid Input! Please try again.")
    else:
        if number_of_words > 6:
            print("That's too many words for a wordle game")
        elif number_of_words < 1:
            print("That's not a positive number of words!")
        else:
            valid_input = True
input_words = []
i = 0
while number_of_words > 0:
    orders = ["first", "second", "third", "forth", "fifth", "sixth"]
    input_word = input(f"What is your {orders[i]} word? ")
    if len(input_word) != 5:
        print("That is not a valid input please try again: ")
        continue
    else:
        input_words.append(input_word)
        number_of_words -= 1
        i += 1
lower_case_words = []
for word in input_words:
    lower_case_words.append(word.lower())
input_words = lower_case_words.copy()    
#### End of input section
    
# guess_combo = ["quick", "brown", "foxxy"]
# The original intention of this project was to find the best 3 words to guess every time, this has failed as
# There are over 280 billion different ways of choosing each combination and it takes about 80 seconds for me to check
# just one word

max_size_of_worst_case = 0
worst_case = ""
# for each answer - find worst case answer - this ties to a variable - size_of_worst_case
# The score of the guess combo is max_size_of_worst_case
# We seek to minimise the score of this variable across all answer combinations

possible_answers_list = []
length_of_super_array = 2
best_word = ""
best_word_score = 2000

# valid_guesses = ["Salet"]  # Check Crane and Qajaj
# for valid_guess in valid_guesses:
#     print(f"Now working on {valid_guess}")
#     max_size_of_worst_case = 0
guess_combinations = [input_words]

now = time.perf_counter()

for guess_combo in guess_combinations:
    print(f"Now working on {guess_combo}")
    for answer in answer_list:  # Starts one of the 2311 games of wordle we could play
        #print(f"Answer is {answer}")
        possible_answers_list = answer_list[:]  # the [:] stops us linking the lists!!
        for word in guess_combo:
            game_output = check_guess(word, answer)
            for poss_answer in possible_answers_list:
                if game_output != check_guess(word, poss_answer):
                    possible_answers_list.remove(poss_answer)
        size_of_worst_case = len(possible_answers_list)

        if max_size_of_worst_case < size_of_worst_case:
            max_size_of_worst_case = size_of_worst_case
            worst_case = answer
            #print(f"worst case is now {answer}, with size {max_size_of_worst_case}")
    print(f"{guess_combo}'s worst opponent is {worst_case} with a max sample size of {max_size_of_worst_case}")

    if max_size_of_worst_case < best_word_score:
        best_word = guess_combo
        best_word_score = max_size_of_worst_case
        print(f"The best words are {guess_combo} with a score of {best_word_score}")

print(f"Time taken = {time.perf_counter() - now}")


# How we made the program faster:
# This was tested on the demo of ["salet","ducky"] and ["salet", "prion]
# salet then prion is a better guess order for those interested
# we calculate the variable game_output once when we add in a new answer
# This makes it
# with: 129 seconds
# without: 166 seconds

# The .lower() function is used twice every time we check guess
# If we just insist our guess combos are capitali(z)ed then this should make the program faster
# we then removed the 2 .lowers() from out function:
# This made a very marginal increase in speed that was not accurately measurable

# Bug found: The wordle answer webpage includes the word "dont" - I dont know how this got through.
# We manually removed the word from the answers textfile
# we manually removed dont then reuploaded the picklefile
#This also increases the code's speed as there is one fewer answer to check

#we removed the print statements as well:

# now it takes 124.6504 seconds! - a decent increase

#Further increases will require us to either increase the efficiency of the code
# or increase the efficiency of the guess checker :(
