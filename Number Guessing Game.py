import random
import time

def welcome_player():
    """Welcomes the player and asks for their name."""
    print("Welcome to the Number Guessing Game!")
    name = input("May I know your name? ")
    print(f"Hi {name}, let's play! I'm thinking of a number between 1 and 200.")
    return name

def pick_number():
    """Generates a random number between 1 and 200."""
    number = random.randint(1, 200)
    return number

def take_guess(name, guesses_taken):
    """Prompts the player for a guess, handles input exceptions, and provides feedback."""
    while True:
        try:
            guess = int(input(f"\nGuess #{guesses_taken + 1}: "))
            if 1 <= guess <= 200:
                return guess
            else:
                print("Your guess must be between 1 and 200. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 200.")

def give_hint(guess, number):
    """Offers a hint if the guess is not correct."""
    difference = abs(guess - number)
    if difference > 50:
        hint = "Much too " + ("high" if guess > number else "low")
    elif difference > 20:
        hint = "Quite a bit " + ("high" if guess > number else "low")
    elif difference > 10:
        hint = "A little " + ("high" if guess > number else "low")
    else:
        hint = "Very close!"
    return hint

def play_game(name):
    """Runs the game loop, tracks guesses, and determines the outcome."""
    number = pick_number()
    guesses_taken = 0
    max_guesses = 6

    while guesses_taken < max_guesses:
        guess = take_guess(name, guesses_taken)
        guesses_taken += 1

        if guess == number:
            print(f"\nCongratulations, {name}! You guessed the number in {guesses_taken} tries.")
            return True  # Indicate successful guess

        hint = give_hint(guess, number)
        print(f"{hint} Try again.")

    print(f"\nSorry, {name}. You ran out of guesses. The number was {number}.")
    return False  # Indicate failed guess

def ask_replay():
    """Asks the player if they want to play again."""
    while True:
        response = input("\nWould you like to play again? (yes/no) ").lower()
        if response in ("yes", "y", "no", "n"):
            return response == "yes" or response == "y"
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")

if __name__ == "__main__":
    name = welcome_player()

    while True:
        if play_game(name):
            print("That was fun! Let's see if you can do it again.")
        else:
            print("Maybe next time you'll be luckier!")

        if not ask_replay():
            break

    print("\nThanks for playing! Come back again soon.")
