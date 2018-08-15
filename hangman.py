
"""
    Hangman game
    Made by: Maria Beatriz Martins
"""

import random
import sys

def game():
    """Main function that runs the game"""
    print("You're about to start playing hangman, I hope you're ready!")
    name = input("Before we start please tell me your name\n")
    print("Now that I know your name lets get started. Please remember that "\
    "your guess must consist of only a letter or the number 1 if you intend" \
    " to guess the entire word.")

    current_try = 0
    max_tries = 6

    while current_try < max_tries:
        flag_guess = 0 #becomes 1 when the guess is valid

        while flag_guess != 1:
            letter_val = validate_guess()
            if letter_val == '1': #if the user pretends to guess the entire word
                try_guess(name)
                flag_guess = 1
            else:
                final_guess = used_letters(letter_val)
                flag_guess = 1

        if letter_val == '1' or not letter_in_word(final_guess):
            current_try += 1
            tries_left = max_tries - current_try
            print("Bad luck, wrong guess. You've got " + str(tries_left) + \
            " tries left.")
            hangman_graphic(current_try)
        else:
            print("That was a great guess!")
            hangman_graphic(current_try)

        current_word(name)

    #message of game over, displayed when the player has used all his tries
    print("Game Over " + name + ". The secret word was " + secret_word + ".")


def secret_word_f():
    """Contains the list of possible categories and then the words associated
    with each category to be used as the secret word. Chooses randomly one of
    the categories and then the secret word"""

    #list of words for each category
    colors = ['red', 'green', 'yellow', 'blue', 'pink', 'purple', 'orange', \
    'aqua', 'beige', 'gray', 'black', 'brown', 'coral', 'gold', 'salmon', \
    'violet', 'magenta', 'lime', 'teal']
    countries = ['croatia', 'singapore', 'hungary', 'ukraine', 'japan', \
    'netherlands', 'macao', 'canada', 'poland', 'portugal', 'greece', \
    'thailand', 'austria', 'malasia', 'mexico']
    animals = ['panda', 'dog', 'cat', 'bison', 'dolphin', 'eagle', 'lobster', \
    'wolf', 'shark', 'crocodile', 'turtle', 'turkey', 'spider', 'monkey', \
    'octopus', 'lion', 'bear', 'cow']
    jobs = ['policeman', 'fireman', 'nurse', 'pilot', 'postman', 'doctor', \
    'waiter', 'teacher', 'secretary', 'journalist', 'engineer', 'architect', \
    'actor', 'dentist', 'farmer']
    food = ['banana', 'orange', 'tomato', 'pasta', 'cheese', 'chocolate', \
    'pizza', 'sandwich', 'eggs', 'potato', 'cereal', 'yogurt', 'chicken', \
    'omelet', 'bacon', 'donut', 'burrito']
    furniture = ['bed', 'wardrobe', 'dresser', 'desk', 'sofa', 'lamp', \
    'chair', 'armchair', 'bookshelf', 'nightstand', 'mirror', 'sink', \
    'curtains', 'picture']
    sports = ['badminton', 'basketball', 'bowling', 'boxing', 'cricket', \
    'football', 'golf', 'gymnastics', 'handball', 'hockey', 'judo', 'surfing',\
     'swimming', 'tennis', 'volleyball']

    list_categories = [colors, countries, animals, jobs, food, furniture, \
    sports]
    list_string = ['colors', 'countries', 'animals', 'jobs', 'food', \
    'furniture', 'sports']

    amount_categories = len(list_categories)
    categories_number = random.randint(0,amount_categories - 1)
    category_final = list_categories[categories_number]
    category_string = list_string[categories_number]

    amount_final_category = len(category_final)
    category_final_number = random.randint(0, amount_final_category - 1)
    return category_final[category_final_number], category_string

def used_letters(letter):
    """Verifies if the user as already done that guess before and if so allows
    him to do another guess. The new guess is then added to the list of used
    guesses"""
    while letter in list_used:
        letter = input("You have already choosen this letter, try another"
        "one!\n")
    list_used.append(letter)
    return letter


def validate_guess():
    """Validates the guess done by the player and allows him to do another
    guess if the one he did was invalid"""
    letter_inval = input("The category is " + str(secret_category) +
    ". Insert your guess or the number 1:\n")
    if letter_inval == '1':
        return letter_inval

    while len(letter_inval) > 1 or not letter_inval.isalpha():
        letter_inval = input("Thats an invalid guess, please insert a new one"
         "\n")

    return letter_inval

def letter_in_word(final_guess):
    return final_guess in secret_word

def current_word(name):
    """Prints out the current word the player has written with his guesses"""
    missing = 0
    print("Your word:")
    lenght = len(secret_word)
    for x in range(0,lenght):
        if secret_word[x] in list_used:
            print(secret_word[x], end="")
        else:
            print("_ ", end ="")
            missing += 1

    print("\n")
    if not missing:
        print("You won " + name + ", congratulations!")
        exit()

def try_guess(name):
    """Allows player to guess the entire word"""
    final_word = input("So you think you know the secret word? Go ahead and do"
    "your guess: ")
    if final_word == secret_word:
        print("You won " + name + ", congratulations!")
        exit()


def hangman_graphic(guess):
    """Draws the current state of the hangman"""
    if guess == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("\n")
    elif guess == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("\n")
    elif guess == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
        print("\n")
    elif guess == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
        print("\n")
    elif guess == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
        print("\n")
    elif guess == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
        print("\n")
    elif guess == 6:
        print("________      ")
        print("|      0      ")
        print("|      |      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")


#global variables
list_used = []
secret_word, secret_category = secret_word_f()

#starts the game
game()
