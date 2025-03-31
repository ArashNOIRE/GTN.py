# The Main game code
#------------------------------------------------------------------
def Hacker():  
    print("################################################")
    print("#    Welcome to Hollywood Hacking Simulator    #")
    print("#                    Play                      #")
    print("#                    Quit                      #")
    print("################################################")
    Uin = str(input("> "))
    if Uin.lower() == "play":
        print("################################################")
        print("#                 Hi Hacker!                   #")
        print("#    Enter your target, like: (FBI or NASA)    #")
        print("################################################")
        Utar = str(input("> "))
        Utarlen = len(Utar)
        increment = 1 / (10 ** Utarlen)
        progress = 0
        print(f"Start Hacking {Utar}")
        while True:
            progress += increment
            print(f"Hacking {Utar}: %{int(progress)}")
            if progress >= 100:
                print(f"{Utar} Hacked successfully!")
                break
    else:
        print("Goodbye")
        exit()
#------------------------------------------------------------------
# Code runner
while True:
    Hacker()
    again = input("Do you want to hack again? (y/n): ")
    if again == "y" or again == "Y":
        continue
    elif again == "n" or again == "N":
        print("Fine, quit then! Hope you weren’t having too much fun.")
        break
    else:
        print("What was that?! I said 'y' or 'n'.")
        continue
#------------------------------------------------------------------
#Finish!

