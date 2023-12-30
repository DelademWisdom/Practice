# **RANDU**
# I want to create a game where the computer generates a random number and the user has to guess it.
# Guides
# 1. The computer will generate a random number from say; 0 and 10
# 2. The user will be asked to guess the number
# 3. If the user guesses the number, the game will end
# 4. If the user does not guess the number, the computer will tell the user if the number is higher or lower than the guess
# 5. The user will be asked to guess again
# 6. If the user guesses the number, the game will end
# 7. This will repeat untill the user guesses the number correctly or quits the game

# How to do it
# Create a function that generates a number randomly from 0 to 10
# Have a fxn that gets the users input (prediction)
# Checks if the generated number equalls the users input and prints an appropriate result
# This should be an infinite loop that ends only when either the user guesses correctly or chooses to end the game

import random
import cowsay
import sys


def main():
    #Welcome Message
    cowsay.cow(
        """
          Hey there, welcome the RANDU!!!!!!
          Let's see how lucky you are!!!
          Guess the number I have in mind
          """
    )

    #Generates random number
    x = number_generator()

    # Loop until user guesses the number
    while True:
        # Get user input
        y = (
            get_number()
        )  
        # print(f"The number = {x}")

        # Checks if user guessed the number
        if y == x:
            cowsay.tux(
                "Hurray, you got it right"
            )  # This is a module that prints out a tux saying (...)
            break

        # Check if user's guess was too high
        elif y > x:
            cowsay.pig(
                "Your number was bigger: Try again"
            )  # This is a module that prints out a pig saying (...)

        # Check if user's guess was too low
        else:
            cowsay.fox(
                "Your number was smaller: Ty again"
            )  # This is a module that prints out a fox saying (...)


# This is a function that generates a random number from 0 to 10
def number_generator():
    return random.randint(0, 10)  # It uses the randint module from the random library


# This is a function that gets the user's input
def get_number():
    while True:  # This is an infinite loop that ends only if the conditions are met
        try:
            user = input("Please choose a number from 0 to 10 or Q / q to quit: ")
            if (user == "Q") or (user == "q"):
                cowsay.turtle(
                    "Sorry to see you go"
                )  # This is a module that prints out a turtle saying (...)
                sys.exit()  # This will quit the whole python script when the Q/q is pressed
            else:
                n = int(user)  # This converts the users input into an integer
                if n < 0 or n > 10:
                    raise ValueError
                return n
        except ValueError:
            cowsay.daemon("Please input a number within the specified range")


if __name__ == "__main__":  # This convert our code to a library
    main()
