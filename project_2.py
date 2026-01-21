# **PROJECT 2 – THE PERFECT GUESS**

# We are going to write a program that generates a random number and asks the user to guess it.

# If the player’s guess is higher than the actual number, the program displays **“Lower number please”**. Similarly, if the user’s guess is too low, the program prints **“higher number please”**. When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

# **Hint:** Use the random module.



import random

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess the number (1 to 100): "))
    guesses += 1

    if guess > number:
        print("Lower number please")
    elif guess < number:
        print("higher number please")
    else:
        print(f"Correct! You guessed it in {guesses} guesses.")
        break
