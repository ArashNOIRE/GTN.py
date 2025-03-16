#Requirements
import random as r
#------------------------------------------------------------------
#Variables
maxanswer = 100
minanswer = 1
answer = r.randint(1, 100)
guess = (int(input("Guess a number between 1 and 100: ")))
attempts = 0
Bounes = 0
#------------------------------------------------------------------
#Guessing & Answering mechanism
while answer != guess:
    if answer > guess:
        print("Too low")
        minanswer = guess
    else:
        print("Too high")
        maxanswer = guess
    guess = (int(input(f"Guess a number between {minanswer} and {maxanswer}: ")))
    attempts = attempts + 1
    Bounes = 1
#------------------------------------------------------------------
#Finish Message
print("WELL DONE!!!")
if Bounes == 0:
    print("WOW you guessed without any Try")
else:
    print(f"You guessed in {attempts} attempts")
#Finish!
