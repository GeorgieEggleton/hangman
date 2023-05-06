import random
import os

guessed_letters = []
word = ""

def opening_screen(word, guessed_letters):
    """
    Welcome text, Expains rules, waits for player to press start
    """
    print("welcome to sailing hangman \n")
    print("Guess the sailing word before the man is hung! \n")

    game_start = input("Press 1 & enter to start \n")
    if game_start == "1":
        word = pickword()
        check_against_word(word, [])
      

    if game_start == "2": 
        display_rules()   
      


def display_rules():
    """
    Display the rules of the game
    """
    print("Test your sailing knowledge \n")
    print("Try to guess the nautical word before the hangman is complete \n")
    print("Type a letter and press Enter \n")
    print("If the letter is in the word it will show \n")
    print("If the letter is not in the word you loose a live and  \n")


def pickword():
    wordlist = ["yacht", "port", "boat", "mast"]
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
    print("User hint" + word)
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





def lives_left(word, guessed_letters):

    lives_left = 3
    for i in guessed_letters:
        if i not in word:
            lives_left -= 1

    if lives_left <= 0:
        print("LOSER!!!!") 
    else:
        
        print("\n")
        print(f"Lives Left = {lives_left}")
        print(f"Letters you've already tried = {guessed_letters}")
        letter_pick_and_validate(word, guessed_letters)     

opening_screen(word, guessed_letters)    



