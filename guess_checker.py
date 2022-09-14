def check_guess(guess, answer):
    # This function takes in a guess string and an answer string - they can include capital letters!
    # The output will look like [2, 1, 2, 0, 0] where
    # 0 is a green letter, 1 is a yellow letter and 2 is a grey letter.
    guess_as_string = guess
    answer_as_string = answer
    guess = list(guess)
    answer = list(answer)
    output = [3, 3, 3, 3, 3]

    for index, letter in enumerate(guess):
        # Check if letter is green STEP 1
        if letter == answer[index]:
            output[index] = 0
            answer_as_string = answer_as_string.replace(letter,"",1)
        elif letter not in answer:  # STEP 2 only checks for grey letters
            output[index] = 2

    for index, letter in enumerate(guess):
        if output[index] == 3:
            # check for orange
            if letter in answer_as_string:
                output[index] = 1
                answer_as_string = answer_as_string.replace(letter, "", 1)
                guess_as_string = guess_as_string.replace(letter, "", 1)
    for index, digit in enumerate(output):
        if digit == 3:
            output[index] = 2 #Any remaining letters are grey

    return output
