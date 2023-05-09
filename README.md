# NAUTICAL HANGMAN


## Nautical hangman is a terminal based Python game in which the user needs to guess the nautical word in 8 lives or less before the man is hung. 

View the live site here - https://nautical-hangman.herokuapp.com/

![Welcome Graphic](/readme-images/welcome-graphic-1.png)
![Welcome Graphic](/readme-images/welcome-graphic-2.png)

### User Experience 
-	The game should be engaging and entertaining. 
-	It should be easy for the user to interact with despite being terminal based
-	It should be informative, by displaying the definition of the word after the round to allow the user to learn the nautical terms. 
-	It should be easy for the user to play multiple rounds of the game. 




### Design flowchart
In order to check my logic for the flow of the game I created the following flow chart. 





### Features

#### Welcome page  
The  welcome graphic features and Ascii art boat and bubble writing game title “Nautical Hangman” As we are developing a terminal based 
game using Ascii art seemed a nice way to make the game more visually interesting. This took a few attempts to dispaly correctly on the mock terminal and in order to show both the image and writting without the user needing to scroll up a 2 second delay was added after the boat image loads before the writting appears. 

![Welcome Graphic](/readme-images/welcome-graphics-together.jpg)

#### Start Options
The player is then presented with 2 options. Press 1 to play the game or press 2 to read the rules. If something other than 1 or 2 is pressed and error massage is shown and it re-prompts them to select 1 or 2. 


#### Rules
If the player presses 2 and enter the rules of the game will be displayed, followed by the option to start the game. 

#### The Game
The game gives the player 7 lives to guess the nautical word. The word will be selected at random from the “words” list. The program will then display underscores for the number of letters in the word. The program will prompt the user to guess a letter. If they guess a correct letter the _ will be replaced with the letters, if they guess incorrectly they loose a life and a limb will be added to the hangman. 

After each guess the letters that the user has guessed will be added to the guessed letters list and displayed on screen to try and help the user guess the word and stop them re-guessing the same letter. If they were to re-guess a letter already tried they would not loose a life but a message will show to tell them they already tried that letter before re-prompting for another letter. 

If the player does not guess the word before the man is hung the loosing message is displayed followed b#uy the complete word and its definition to help the player learn the nautical terms. 

If the player does guess the word before the man is hung the winning message is displayed followed by the word and definition. 

After the end of each round the game will ask the player if they would like to play again. If they press Y the game will be re-loaded with a new random word. If they press N the game will exit. 


## Future Features
- In future additions I would like to a google sheet API to save the users scores so they can return and try to beat their last score
- I would like to add the option for the user to pick a difficulty level (based on the number of letters in the word), this means the game could be targetted at mulitiple different age groups easier. 

## Testing
I ran the code through the Code Insitute python validator. A number of errors were picked up, mostly mnor issues such as trailing white space, lines too long, or too many line breaks. I have corrected all of these and the code now passes the validator with no errors found. 

![Welcome Graphic](/readme-images/validator_screenshot.png)

### BUGS
On deployment to the Heroku mock terminal I found that the welcome graphic was too wide and broke. I therefore had to update the graphic to be less than 80 characters wide to ensure it fitted. 
I also needed to move the Graphics "Nautical" and "Hangman" on to two seperate lines to ensure they fitted into the mcok terminal. 

On delpoyment I found that if the image and words loaded at the same time the image was pushed up in the terminal out of view unless the user scrolled up. I therefore decided to load the boat graphic first, give a 2 second delay, then load the writting to give a better aesthetic.  















Made a decision that the guessed letters should be in guessed order not aplbetical order
Test letters in guessed letters array not in order
Made game text sit along side hangman graphic



Bugs- 
Input needs to be uppercase
