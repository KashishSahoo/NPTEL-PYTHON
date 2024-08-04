import random

account=0
for i in range(30):
    # bet=int(input("Enter Your Bet="))
 bet=random.randint(1,10)
 lucky_draw=random.randint(1,10)
 print("Bet:",bet)
 print("Lucky_draw:",lucky_draw)
 

 if bet==lucky_draw:
    account=account+900-100
 else:
    account=account-100

 print("Money In Account=",account) 