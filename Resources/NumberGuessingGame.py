
import random
# Generate random Number
secret = random.randint(1, 10)
# set guess to zero
guess = 0
# set tries to zero
tries = 0
# set while loop
while guess != secret and tries < 5:

    guess = int(input("Enter your guess: "))

    if guess < secret:
        print("You guess is too low")
    elif guess > secret:
        print("Your guess is too high")

    tries += 1
# if guess == secret --> you won
if guess == secret:
    print("You Won.it took you ", tries, " tries to guess that number")
#else you lost
else:
    print("Oops..You lost. No turns left!")