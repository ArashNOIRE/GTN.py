# Requirements
import random as r
#------------------------------------------------------------------
def main():  # The Main game code
    # Variables
    maxguess = 100
    minguess = 1
    rnguess = r.randrange(minguess, maxguess)
    attempts = 0
    bounes = 0
    #------------------------------------------------------------------
    # Guessing & Answering mechanism
    print (f"this is your number: {rnguess}")
    answer = input("my guess is right?")
        # ^^^answer must be + or - or = .^^^
    while answer != "=":
        if answer == "+":
            minguess = rnguess
            rnguess = r.randrange(minguess, maxguess)
        elif answer == "-":
            maxguess = rnguess
            rnguess = r.randrange(minguess, maxguess)
        print (f"my guess is {rnguess}")
        answer = input("my guess is right?")
        attempts = attempts + 1
        bounes = 1
    #------------------------------------------------------------------
    # Finish Message
    print ("Nice")
    if bounes == 0:
        print("WOW I guessed it without any Try!")
    else:
        print(f"I guessed it in {attempts} attempts.")
# End of the game code
#------------------------------------------------------------------
while True:  # Code runner
    main()
    again = input("Would you like to play again? (y/n): ")
    if again == "y":
        continue
    else:
        print("Thank you for playing")
        break


#Finish!