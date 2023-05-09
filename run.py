import random
import os
from graphics import welcome_graphic
from graphics import hangman
import time
from words import words
from words import definition

guessed_letters = []
word = ""
wordlist = words
for i in range(len(wordlist)):
    wordlist[i] = wordlist[i].upper()


def opening_screen(word, guessed_letters):
    """
    Displays welcome graphic 1, waits 2 seconds displays welcome graphic 2.
    and triggers game_start
    """
    print(welcome_graphic[0])
    time.sleep(2)
    print(welcome_graphic[1])
    print("welcome to sailing hangman \n")
    print("Guess the sailing word before the man is hung! \n")
    game_start(word, guessed_letters)


def game_start(word, guessed_letters):
    """
    Displays options to start the game, display the rules or exit
    """
    start = input("Press 1 & enter to start or 2 & enter to read the rules \n")
    start = start.strip(" ")
    if start == "1":
        word = pickword()
        check_against_word(word, [])

    elif start == "2":
        display_rules(word, guessed_letters)

    elif start == "3":
        exit()

    else:
        print("""You need to press 1 or 2 and 'Enter' to either start the game
 or display the rules \n""")
        game_start(word, guessed_letters)


def display_rules(word, guessed_letters):
    """
    Display the rules of the game
    """
    print("Test your sailing knowledge \n")
    print("Try to guess the nautical word before the hangman is complete \n")
    print("Type a letter and press Enter \n")
    print("If the letter is in the word it will show \n")
    print("""If the letter is not in the word you loose a live and get closer
 to hanging the man\n""")
    print("GOOD LUCK!!\n")
    game_start(word, guessed_letters)


def pickword():
    """
    Picks a word at random from the word list and capitlizes it
    """
    word = random.choice(wordlist)
    print(word)
    return word.upper()


def letter_pick_and_validate(word, guessed_letters):
    """
    Prompts the user to pick a letter
    Checks if it is a letter
    If not a letter returns Error message and asks them to try again
    """
    current_letter = input("Pick a letter \n")

    if current_letter.isalpha():
        check_letter(word, guessed_letters, current_letter.upper())
    else:
        print("not a letter")
        letter_pick_and_validate(word, guessed_letters)


def check_letter(word, guessed_letters, current_letter):
    """
    Takes the letter picked by the user and checks if its been used before
    Adds the new letter to the guessed letters list
    """
    if current_letter in guessed_letters:
        print("You already guessed that letter")
        letter_pick_and_validate(word, guessed_letters)

    else:
        guessed_letters.append(current_letter)
        check_against_word(word, guessed_letters)


def check_against_word(word, guessed_letters):
    """
    Clears the terminal to keep game space clear and readable
    Checks each letter of the word in turn to see
    if the guessed letter is there
    Displays the letter in the correct place
    If the word is complete displays winning message, word and definition
    """
    os.system("clear")
    display_word = ""
    for i in word:
        if i in guessed_letters:
            display_word += i + " "
        else:
            display_word += "_ "
    print(display_word)
    if "_" in display_word:
        lives_left(word, guessed_letters)
    else:
        print("YOU WIN!!!")
        wordnum = wordlist.index(word)
        worddef = definition[wordnum]
        print(f"{word} - {worddef}\n")
        time.sleep(1)
        play_again_option(word, guessed_letters)


def lives_left(word, guessed_letters):
    """
    Updates lives left and displays next hangman life if incorrect guess.
    If lives left gets to 0 display loosing message, word and definition
    Give player the option to try again
    """
    lives_left = 7
    for i in guessed_letters:
        if i not in word:
            lives_left -= 1
    if lives_left <= 0:
        print(hangman[7])
        print("Oh no! You Lose!\n")
        wordnum = wordlist.index(word)
        worddef = definition[wordnum]
        print(f"{word} - {worddef}\n")
        time.sleep(1)
        play_again_option(word, guessed_letters)
    else:
        print(hangman[7 - lives_left])
        print("\n")
        print(f"Lives Left = {lives_left}")
        print(f"Letters you've already tried = {guessed_letters}")
        letter_pick_and_validate(word, guessed_letters)


def play_again_option(word, guessed_letters):
    """
    Add option to play again after winning or losing.
    """
    play_again = input("Would you like to play again? Y/N \n")
    play_again = play_again.strip(" ")
    play_again = play_again.capitalize()
    if play_again == "Y":
        opening_screen(word, guessed_letters)

    elif play_again == "N":
        print("Thanks for playing, come back soon!")
        exit()

    else:
        print("Not an Option Pick Y or N")
        play_again_option(word, guessed_letters)


opening_screen(word, guessed_letters)
