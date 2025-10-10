import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)

def play_blackjack():
    print(logo)

    usercards = []
    computer_cards = []
    for _ in range(2):
        usercards.append(deal_card())
        computer_cards.append(deal_card())

    userscore = calculate_score(usercards)
    computer_score = calculate_score(computer_cards)
    is_game_over = False

    while not is_game_over:
        userscore = calculate_score(usercards)
        print(f"Your cards: {usercards}, current score: {userscore}")
        print(f"Computer's first card: {computer_cards[0]}")

        if userscore == 0 or computer_score == 0 or userscore > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to hit, 'n' to stand: ").lower().strip()
            while choice not in ("y", "n"):
                choice = input("Invalid input. Type 'y' to hit, 'n' to stand: ").lower().strip()
            if choice == "y":
                usercards.append(deal_card())
            else:
                is_game_over = True

    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {usercards}, final score: {userscore}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if userscore == computer_score:
        print("Draw")
    elif computer_score == 0:
        print("You lose, opponent has Blackjack!")
    elif userscore == 0:
        print("Win with a Blackjack!!")
    elif userscore > 21:
        print("You went over. You lose, womp womp.")
    elif computer_score > 21:
        print("Opponent went over. You win, nice!")
    elif userscore > computer_score:
        print("You win slick.")
    else:
        print("You lose, sit.")

while True:
    play_blackjack()
    again = input("\nDo you want to play another round? Type 'y' or 'n': ").lower().strip()
    while again not in ("y", "n"):
        again = input("Invalid input. Please type 'y' or 'n': ").lower().strip()
    if again == "n":
        print("\nThanks for playing BlackJack!")
        break