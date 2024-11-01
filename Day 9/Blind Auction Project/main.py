# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
print(logo)

other="yes"

def find_highest_bidder(bid):
    highest_bid=0
    winner=""
    for key in bid:
        bid_amount=bid[key]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=key

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids={}
while other == "yes":
    name = input("What is your name? :")
    price = int(input("What is your price? :$"))

    bids[name] = price
    other = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if other == "no":
        find_highest_bidder(bids)
    elif other == "yes":
        print("\n" * 20)

print(bids)
