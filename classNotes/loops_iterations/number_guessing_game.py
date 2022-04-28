'''     Number Guessing game

1. Start
2. Generate a secret number between 1 and 10
3. Set the user guess = 0
4. Set tries = 0
5. While user guess is not equal to secret and number of tries is less than 5:
    1. Take the user guess from user
    2. If user guess is less than secret
        1. Display the message "Your guess is too low"
    3. Otherwise if user gues is greater than secret
        1. Display message "Your guess is too high"
    4. Increase number of tries by 1 (tries= tries + 1)
6. If user guess == secret
    1. Display message "Tou won". It took you XXX tries to guess that number
7. Otherwise, display message "Oops, you lost. No turns left"


        main
          |
    interger secret
        |
    interger quess
        |
    quess = 0
        |
    secret = 0
        |
secret != guess and tries = 5 __True_____________
        |   ^                                   |
  False |   |                              input guess
        |   |                                   |
        |   |               _______False__guess = secret__True__
        |   |               |                                   |
        |   |       Output "Your guess is too high"   Output "Your guess is to low"
        |   |               |___________________0_______________|
        |   |                                   |
        |   |                            tries = tries +                   
        |   |___________________________________0
        \
         \
          \
           \
            \
             \
              \
__False____guess = secret__True_____
|                                   |
Output "You lost"              Output = "You won"
|_________________0_________________|
                  |
                 End

'''
import random
# Generate random Number
secret = random.randint(1, 10)
#  set the guess to Zero
guess = 0
# set tries to zero
tries = 0
# set while loop
while guess != secret and tries < 5:
    
    guess = int(input("Enter your guess: "))
    
    if guess < secret:
        print ("Your guess is too low")
    elif guess > secret:
        print("Your guess is too high")
    
    tries += 1
# if guess  == secret --> you won
if guess == secret:
    print("You Won. It took you ", tries, " tries to guess that number")
# else you lost
else:
    print("Oops. You lost, no more turns left ")  # Enter your guess: 1
                                                # Your guess is too low
                                                # Enter your guess: 3
                                                # Your guess is too high
                                                # Enter your guess: 6
                                                # Your guess is too high
                                                # Enter your guess: 5                                             
                                                # Your guess is too high
                                                # Enter your guess: 2
                                                # Your guess is too high
                                                # You Won. It took you  5  tries to guess that number
