import random
#import gspread
#from google.oauth2.service_account import Credentials
import os
from graphics import welcome_graphic 
from graphics import hangman
import time

"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file(creds.json)
SCOPED_CREDS = CREDS.with_scopes(scope)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('words')
""" 

guessed_letters = [] 
word = ""
wordlist = ["YACHT", "PORT", "BOAT", "MAST", "BAGGYWRINKLE"]
definition = ["a floating thing", "the left", "A small flaoting thing", "The stick", "something Owain doesn't know"]

def opening_screen(word, guessed_letters):
    """
    Welcome text, Expains rules, waits for player to press start
    """
    print(welcome_graphic[0])
    time.sleep(2)
    print(welcome_graphic[1])

    print("welcome to sailing hangman \n")
    print("Guess the sailing word before the man is hung! \n")
    game_start(word, guessed_letters)


def game_start(word, guessed_letters):
    start = input("Press 1 & enter to start or 2 & enter to read the rules \n")
    if start == "1":
        word = pickword()
        check_against_word(word, [])
   
    elif start == "2": 
        display_rules(word, guessed_letters)   
   
    else:
        print("You need to press 1 or 2 and 'Enter' to either start the game or display the rules")
        game_start(word, guessed_letters)



def display_rules(word, guessed_letters):
    """
    Display the rules of the game
    """
    print("Test your sailing knowledge \n")
    print("Try to guess the nautical word before the hangman is complete \n")
    print("Type a letter and press Enter \n")
    print("If the letter is in the word it will show \n")
    print("If the letter is not in the word you loose a live and get closer to hanging the man\n")
    print("GOOD LUCK!!\n")
    game_start(word, guessed_letters)



def pickword():

    word = random.choice(wordlist)
    print(word)
    return word.upper()
    
   






def letter_pick_and_validate(word, guessed_letters):
    
    current_letter = input("Pick a letter \n")   
    
    if current_letter.isalpha():
        
        check_letter(word, guessed_letters, current_letter.upper())
    else:
        print("not a letter")
        letter_pick_and_validate(word, guessed_letters)
        


def check_letter(word, guessed_letters, current_letter):
    
    if current_letter in guessed_letters:
        print("You already guessed that letter")
        letter_pick_and_validate(word, guessed_letters)
       
    else:
        guessed_letters.append(current_letter)
        check_against_word(word, guessed_letters) 



def check_against_word(word, guessed_letters):
    os.system("clear")
    display_word = ""
    for i in word:
        if i in guessed_letters:
            display_word += i +" "
 
        else:
            display_word += "_ "
            
    print(display_word)
    if "_" in display_word:
        lives_left(word, guessed_letters)
    else:    
        print("YOU WIN!!!")
        wordnum = wordlist.index(word)
        worddef = definition[wordnum]
        print(f"{word} - {worddef}")






def lives_left(word, guessed_letters):

    lives_left = 7
    for i in guessed_letters:
        if i not in word:
            lives_left -= 1
   
    if lives_left <= 0:
        print("You Lose!") 
        print(hangman[7])
        wordnum = wordlist.index(word)
        worddef = definition[wordnum]
        print(f"{word} - {worddef}")
    else:
        print(hangman[7 - lives_left])
        print("\n")
        print(f"Lives Left = {lives_left}")
        print(f"Letters you've already tried = {guessed_letters}")
        letter_pick_and_validate(word, guessed_letters)     

opening_screen(word, guessed_letters)    



