import random

possibleWords = ["apple", "shoe", "icecream", 'pringles']
resultString = []
chosenWord = random.choice(possibleWords)
gameOver = False
numberOfPossibleAttempts = 6

print(chosenWord)
for character in range(len(chosenWord)):
    resultString += "_"
print(resultString)
while not gameOver:
    guessedLetter = input("Guess a missing letter: ").lower()
    for position in range(len(chosenWord)):
        if chosenWord[position] == guessedLetter:
            resultString[position] = guessedLetter
    print(resultString)

    if guessedLetter not in chosenWord:
        numberOfPossibleAttempts -= 1
        if numberOfPossibleAttempts == 0:
            print("You lost. The hangman died")
            gameOver = True

    if '_' not in resultString:
        print("You saved the hangman congratulations!!")
        gameOver = True

