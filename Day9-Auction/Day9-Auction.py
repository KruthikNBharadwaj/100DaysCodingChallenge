from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
auction={}
bidding=True

def find_max(bid_rec):
  highest=0
  winner=""
  for bidder in bid_rec:
    amt=int(bid_rec[bidder])
  if amt>highest:
    highest=amt
    winner=bidder
  print(f"The winner is {winner} with the bid amount of ${highest}")
  
while bidding:
  name=input("Enter your name:\n")
  bid_amt=input("Enter your bid amount $")
  auction[name]=bid_amt
  #print(auction)
  extra=input("Are there any other bidders? Type Yes or No").lower()
  if extra=="no":
    bidding=False
    find_max(auction)
  elif extra=="yes":
    clear()