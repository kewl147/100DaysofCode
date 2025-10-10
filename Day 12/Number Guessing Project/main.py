import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")

def easy_mode():
    return 10

def hard_mode():
    return 5

def play_game():
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    while True:
        mode = input("Choose a difficulty ('easy' or 'hard'): ").lower().strip()
        if mode in ("easy", "hard"):
            break
        print("Invalid choice. Please type 'easy' or 'hard'.")

    attempts = easy_mode() if mode == "easy" else hard_mode()

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == number:
            print(f"You got it! The number was {number} ")
            break
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")

        attempts -= 1

        if attempts == 0:
            print(f"Out of guesses! The number was {number}. ")

    play_again = input("\nPlay again? (y/n): ").lower().strip()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

play_game()
