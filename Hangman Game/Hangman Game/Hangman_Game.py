import random


def Game():
    print ("\nWelcome... This is a hangman game.\nYou have 6 attempts to guess the word.\nGoodluck!!!\n")
    listOfWords = ["samuel", "sodji", "ruth", "bridget", "ernestina", "elyon"]

    secretWord = random.choice(listOfWords)

    output = []

    liveScore = 6

    gameOver = False
    for character in range(len(secretWord)):
        output += '_'
    print(output)

    while not gameOver:
        userGuess = input("Guess a letter: ").lower()
        for position in range(len(secretWord)):
            if secretWord[position] == userGuess:
                output[position] = userGuess
        print(output)
        
        if userGuess not in secretWord:
            liveScore -= 1
            if liveScore == 0:
                print("\nYou lost the hangman died")
                gameOver = True
       
        if "_" not in output:
            print("\nCongratulations you saved the hangman!!!!! \n")
            gameOver = True
            
response = int(input("\nWould you like to play a game?\n1. Yes\n2. No\nUser response: "))

if response == 1:
    Game()
    
elif response == 2:
    print("\nSad to see you leave...\nHope you return soon!\n")
    

