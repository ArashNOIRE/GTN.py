# Requirements
import random as r
#------------------------------------------------------------------
def dice_roller(): # The Main game code
    dice = r.randint(1, 6)
    print(f"The dice rolled... {dice}!")
#------------------------------------------------------------------
while True:  # Code runner
    dice_roller()
    again = input("Do you want to roll the dice again? (y/n): ")
    if again == "y" or again == "Y":
        continue
    elif again == "n" or again == "N":
        print("Fine, quit then! Hope you weren’t having too much fun.")
        break
    else:
        print("What was that?! I said 'y' or 'n'. Stop rolling off-script and roll the dice!")
        continue
#Finish!