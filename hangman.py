# hangman game

import random

def hangman_game(words):
# Function will choose one random
    # word from this list of words
    word = random.choice(words)
    guessedWord2 = []
    
    guesses = ''
    
    wrongGuess = 0;

    # In this game, the user has unlimited chances   
    
    while True:
        
        # a constant to make sure the game can end
        failed = 0
        
        # all characters from the input
        # word taking one at a time.
        guessedWord = []
        for char in word:
            # comparing that character with
            # the character in guesses
            if char in guesses:
                # print(char)
                guessedWord.append(char)

                
            else:
                # print("*")
                guessedWord.append("*")
                failed += 1
        
        # put the all guessed values in here
        # to check later if a new guessed value has been 
        # inputed already
        guessedWord2 = guessedWord


        
        if failed == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            print("The word is", str(word), ". You missed", +wrongGuess, 'time')

            # ask user if they want to play again
            anotherTry = input("Do you want to guess another word? Enter y or n >")

            if anotherTry is 'n':
                break
            else:
                return hangman_game(words)
        
        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("(Guess) Enter a letter in word " +str("".join(guessedWord))+ " > " )
        
        # every input character will be stored in guesses
        guesses += guess
        
        # check to see if the letter in the word has been displayed already
        if guess in guessedWord2:
            print(str(guess), "is already in the word")

        # check to see if input corresponds to any character in the word
        if guess not in word:
            wrongGuess +=1
            print(str(guess), "is not in the word")
            

if __name__ == "__main__":
    # List of words in the game
    # This can be better by using random-word generator
    words = ["write", "program", "that", "receive", "positive", "change", "study", "excellent", "nice"]
    hangman_game(words)
    