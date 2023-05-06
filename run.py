import random

guessed_letters = []

def opening_screen():
    """
    Welcome text, Expains rules, waits for player to press start
    """
    print("welcome to sailing hangman \n")
    print("Guess the sailing word before the man is hung! \n")

    game_start = input("Press 1 & enter to start \n")
    if game_start == "1":
        word = pickword()
        play_game(word)

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
    wordlist = ["yacht", "boat", "mast"]
    word = random.choice(wordlist)
    return word.upper()
   

def play_game(word):
    
    blank_word = "_ " *len(word)   
    lives = 10
    print(blank_word + "\n")
    print(lives)




def letter_pick_and_validate(guessed_letters):
    current_letter = input("Pick a letter \n")   
    
    if current_letter.isalpha():
        print("checking against word")
        check_letter(current_letter, guessed_letters)
    else:
        print("not a letter")
        letter_pick_and_validate(guessed_letters)
        


def check_letter(current_letter, guessed_letters):
    if current_letter in guessed_letters:
        print("You already guessed that letter")
        letter_pick_and_validate()
       
    else:
        #check_against_word() 
        guessed_letters.append(current_letter)



def check_against_word(guessed_letters, word):
    display_word = ""
    for i in word:
        if i in guessed_letters:
            display_word += i +" "
 
        else:
            display_word += "_ "
    print(display_word)

"""
opening_screen()    
letter_pick_and_validate(guessed_letters)
"""





check_against_word(["a", "c"], "yacht")
    












    
