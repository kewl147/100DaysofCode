import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

while True:
    chosen_word = random.choice(word_list)
    print(chosen_word)
    display = ["_"] * len(chosen_word)
    lives = len(stages) - 1
    guess_counts = {}

    print(" ".join(display))

    while "_" in display and lives > 0:
        guess = input("Guess a Letter?: ").lower()

        if not (len(guess) == 1 and guess.isalpha()):
            print("Please enter a single letter (a–z).")
            continue

        penalize = False
        if guess in guess_counts:
            if guess_counts[guess] == 1:
                print(f"You already guessed '{guess}' once. Next repeats will cost a life!")
            else:
                print(f"You guessed '{guess}' again! You lose a life.")
                penalize = True
        guess_counts[guess] = guess_counts.get(guess, 0) + 1

        if guess in chosen_word:
            for position, character in enumerate(chosen_word):
                if character == guess:
                    display[position] = guess
            print("Correct!")
        else:
            if not penalize:
                print("Incorrect!")
                penalize = True

        if penalize:
            lives -= 1

        print(" ".join(display))
        print(stages[lives])

    if "_" not in display:
        print(f"🎉 You win! The word was: {chosen_word}")
    else:
        print(f"💀 You lose! The word was: {chosen_word}")

    while True:
        again = input("Play again? (y/n): ").lower()
        if again in ["y", "n"]:
            break
        print("Please type 'y' or 'n'.")

    if again == "n":
        print(r"""
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
        """)
        break
