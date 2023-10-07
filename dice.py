import random 

again = True

while again: 
    print(random.randint(1,6))
    dice_roll = input("Do you want to roll the dice again? (y/n) :")
    if dice_roll.lower() == "y":
        continue
    else:
        break