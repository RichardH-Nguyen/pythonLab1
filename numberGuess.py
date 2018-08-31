import random
x = random.randint(1, 101)

playerGuess = int(input('Guess a number!'))

while playerGuess != x:
    try:
        if playerGuess > x:
            playerGuess = int(input('Too high! Guess again!'))
        elif playerGuess < x:
            playerGuess = int(input('Too low! Guess again!'))
    except ValueError:
        playerGuess = int(input('Not a number! Guess again!'))

print("correct! CPU: " + str(x) + "\n Your Guess: " + str(playerGuess))