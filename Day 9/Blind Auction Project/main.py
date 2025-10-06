# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
print("Welcome to the Silent Auction")

bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = -1
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bidding_finished = False

while not bidding_finished:
    name = input("Enter your name:\n").lower()

    # ✅ Validate bid input
    while True:
        bid_input = input("Enter your bid:\n$").strip()
        if bid_input.isdigit():
            bid = int(bid_input)
            break
        else:
            print("Invalid bid. Numbers only, no spaces or symbols.")

    bids[name] = bid
    print("\n" * 50)  # simulate clear screen immediately after bid

    # ✅ Validate yes/no input
    while True:
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
        if more_bidders in ["yes", "no"]:
            break
        print("Invalid input. Please type 'yes' or 'no'.")

    if more_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
