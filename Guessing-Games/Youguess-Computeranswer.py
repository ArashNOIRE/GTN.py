# Requirements
import random as r
#------------------------------------------------------------------
def main():  # The Main game code
    # Variables
    maxanswer = 100
    minanswer = 1
    answer = r.randint(1, 100)
    guess = (int(input("Guess a number between 1 and 100: ")))
    attempts = 0
    bounes = 0
    #------------------------------------------------------------------
    # Guessing & Answering mechanism
    while answer != guess:
        if answer > guess:
            print("My number is bigger")
            minanswer = guess
        else:
            print("My number is smaller")
            maxanswer = guess
        guess = (int(input(f"Guess a number between {minanswer} and {maxanswer}: ")))
        attempts = attempts + 1
        bounes = 1
    #------------------------------------------------------------------
    # Finish Message
    print("WELL DONE!!!")
    if bounes == 0:
        print("WOW you guessed without any Try")
    else:
        print(f"You guessed in {attempts} attempts")
    print("Game finished")
# End of the game code
#------------------------------------------------------------------
while True:  # Code runner
    main()
    again = input("Do you want to play again? (y/n): ")
    if again == "y" or again == "Y":
        continue
    elif again == "n" or again == "N":
        print("Fine, quit then! Hope you weren’t having too much fun.")
        break
    else:
        print("What was that?! I said 'y' or 'n'.")
        continue

#Finish!