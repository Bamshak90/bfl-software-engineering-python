'''
Process to Build the Game

Game Setup

Decide on a range of numbers (for example, 1 to 100).

Generate a random secret number within that range.

Ask the player how many attempts (chances) they want to play with.

Game Loop (while loop)

While the player still has attempts left:

Ask them to guess a number.

If the guess is correct → congratulate them and break the loop.

If the guess is wrong:

Tell them if the guess is too high or too low.

Reduce the remaining attempts.

Challenge with for loop

After the game ends (win or lose), display the entire history of their guesses.

Use a for loop to print out each guess in order.

Extra Challenge Ideas (to make it trickier):

Give hints like: "The number is divisible by 3" or "The number is even/odd" after certain wrong attempts.

Add a scoring system (more points for fewer attempts).

Allow the user to play multiple rounds until they quit.
'''

import random
guess_limit = 1
attempt = int(input("How many time do you want to play: "))


while guess_limit <= attempt:
    random_number = random.randint(1,3)
    guess = input(input("Enter the guessed number: "))
    guess_limit += 1
    if guess == random_number:
      print("Hooray you won the game")
    else:
       print("You have failed")
    

