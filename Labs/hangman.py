# Hangman game

# PSEUDOCODE
# setup your game by doing the following
# make a word list for your game
# grab a random word from your list and store it as a variable

# in a loop, do the following
# display the hangman using the gallows
# display the used letters so the user knows what has been selected
# display the length of the word to the user using blank spaces and used letters
# prompt the user to guess a letter
# don't allow the user to select the same letter twice
# if the guess is incorrect increment incorrect_guesses by 1
# if the incorrect_guesses is greater than 8, tell the user they lost and exit the program
# if the user gets all the correct letters, tell the user they won

# ask if they want to play again
import math
import random

over = False
gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

frame = 0
guessed_letters = []
guessed_letters_wrong = []
word_guess = []
word_list = ["Potato", "Pizza", "French", "Computer", "philanthropist", "mountain", "Golden", "Calendar"]
word_number = random.randrange(len(word_list))
word = word_list.pop(word_number)

word_hit_list = []
hit_list_goal = []
for i in word:
    word_guess.append("_")
    word_hit_list.append("place holder")
    hit_list_goal.append("x")
while over == False:
    # Drawing code:
    print(gallows[frame])
    print(*guessed_letters_wrong)
    print(*word_guess)
    # rest of code
    letter_guessed = input("Guess a letter...")
    rerun = False
    for i in guessed_letters:
        if i.lower() == letter_guessed.lower():
            print("\nLetter already chosen.\n")
            rerun = True
    while rerun == True:
        letter_guessed = input("Guess a letter...")
        for i in guessed_letters:
            if i.lower() == letter_guessed.lower():
                print("\nLetter already chosen.\n")
            else:
                rerun = False
    guessed_letters.append(letter_guessed)
    trigger = False
    for i in range(len(word)):
        if word[i].lower() == letter_guessed.lower():
            word_guess[i] = letter_guessed
            word_hit_list[i] = "x"
            trigger = True
    if trigger == False:
        guessed_letters_wrong.append(letter_guessed.upper())
        frame += 1
    if frame >= 6:
        print("You have died!!")
        break
    if word_hit_list == hit_list_goal:
        print(gallows[frame])
        print(*guessed_letters_wrong)
        print(*word_guess)
        print("\nCongratulations!! \n \r You win!")
        again = input("\nDo you want to play again? \n\r Yes or No?..")
        if again.lower() == "yes":
            word_number = random.randrange(len(word_list))
            word = word_list.pop(word_number)
            word_hit_list = []
            hit_list_goal = []
            frame = 0
            guessed_letters = []
            guessed_letters_wrong = []
            word_guess = []
            for i in word:
                word_guess.append("_")
                word_hit_list.append("place holder")
                hit_list_goal.append("x")
        else:
            break

