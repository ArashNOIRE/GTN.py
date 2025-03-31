# Requirements
import random as r
#------------------------------------------------------------------
# The Main game code
def slot_machine(chips):
    # Variables
    symbols = ["$", "*","*", "@","@","@", "%","%","%","%","#","#","#","#","#"]
    reel1_symbol = r.choice(symbols)
    reel2_symbol = r.choice(symbols)
    reel3_symbol = r.choice(symbols)
    spin_count = 0
    chips -= 50
    #------------------------------------------------------------------
    # slot machine mechanism
    while True:
        spin_count += 1
        print(f"{reel1_symbol} {reel2_symbol} {reel3_symbol} \n")
        reel1_symbol = r.choice(symbols)
        reel2_symbol = r.choice(symbols)
        reel3_symbol = r.choice(symbols)
        if spin_count == 9999:
            print ("This is your result: ")
            print(f"{reel1_symbol} {reel2_symbol} {reel3_symbol}")
            if reel1_symbol == reel2_symbol == reel3_symbol:
                print ("You won!")
                if reel1_symbol == reel2_symbol == reel3_symbol == "$":
                    chips += 500
                    print ("You earn 500")
                elif reel1_symbol == reel2_symbol == reel3_symbol == "*":
                    chips += 250
                    print ("You earn 250")
                elif reel1_symbol == reel2_symbol == reel3_symbol == "@":
                    chips += 100
                    print ("You earn 100")
                elif reel1_symbol == reel2_symbol == reel3_symbol == "%":
                    chips += 50
                    print ("You earn 50")
                elif reel1_symbol == reel2_symbol == reel3_symbol == "#":
                    chips += 25
                    print ("You earn 25")
            elif reel1_symbol == reel3_symbol or reel2_symbol == reel1_symbol or reel3_symbol == reel2_symbol:
                print ("It's real close but you lose!")
                chips += 5
                print("You earn 5")
            else:
                print ("Loser!")
            break
    return chips
#------------------------------------------------------------------
# Code runner
chips = 1000
while True:
    chips = slot_machine(chips)
    if chips < 50:
        break
    print(f"you have {chips} chips!")
    again = input("Again? (y/n): ")
    if again == "y" or again == "Y":
        continue
    elif again.lower() == "hesoyam":
        if 50 < chips <= 100:
            chips += 250000
            print("Oh sorry, I almost forgot you are VIP! enjoy your game")
        else :
            print("Don't go fast!")
            chips = 50

        print(f"you have {chips} chips!")
    elif again == "n" or again == "N":
        print("Fine, quit then! Hope you weren’t win.")
        break
    else:
        print("What was that?! I said 'y' or 'n'.")
        continue
#------------------------------------------------------------------
# Finish!