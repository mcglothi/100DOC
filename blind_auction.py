import os
from auction_art import logo
print(logo)
print("Welcome to the secret auction program.")
auctions = {}
auctions_end = False
while not auctions_end:
  name = input("What is your name?: ")
  bid = float(input("What's your bid?: $"))
  auctions[name] = bid
  other_bidders = input("Are there any other bidders? Type 'y' or 'n'.\n").lower()
  if other_bidders == "n":
    auctions_end = True
    os.system('clear')
  elif other_bidders == "y":
    os.system('clear')
  else:
    input("Please type only 'y' or 'n': ").lower()
winner = ""
winner_bid = 0
for bidder in auctions:
  if auctions[bidder] > winner_bid:
    winner_bid = auctions[bidder]
    winner = bidder
print(f"The winner is {winner} with a bid of ${winner_bid}.")

