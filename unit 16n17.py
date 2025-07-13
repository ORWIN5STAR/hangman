import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getstart():
    print("The menu options are: ")
    print("  1. Play")
    print("  2. Display Instructions and")
    print("  3. Quit.")
    x = int(input("Choose options: "))

    if(x == 1):
        clear()
        run()
    elif x == 2:
        clear()
        print("Game Play")
        print("Players try and guess all of the letters in a secret word. ")
        print("As they guess correctly, letters are revealed in the secret word. ")
        print("However, players can only guess an incorrect letter five times. ")
        print("If the user guesses the secret word in time, then they won, otherwise they lost. ")
        
    elif x == 3:
        exit()

def getoption():
    print("The menu options are: ")
    print("  1. Play Again")
    print("  2. Display Instructions and")
    print("  3. Quit.")
    x = int(input("Choose options: "))

    if(x == 1):
        clear()
        run()
    elif x == 2:
        clear()
        print("Game Play")
        print("Players try and guess all of the letters in a secret word. ")
        print("As they guess correctly, letters are revealed in the secret word. ")
        print("However, players can only guess an incorrect letter five times. ")
        print("If the user guesses the secret word in time, then they won, otherwise they lost. ")
        
    elif x == 3:
        exit()

def get_words(ml):
    list = []
    for i in range(0, len(ml)):
        x = ml[i]
        list.append(x)

    return list

def get_dot(ml):
    dot = []
    for i in range(0, len(ml)):
        dot.append("*")

    return dot

def run():
    newlist = ["Cat", "Elephant", "Pets", "Dogs", "Phone", "Basketball", "Soccer", "Coke"]
    ml = random.choice(newlist)
    guessList = []

    storelist = get_words(ml)
    length = str(len(ml))
    dot = get_dot(ml)
    dot1 = " ".join(dot)
    Maxguess = False
    a = 0

    print("Welcome to Word Guesser!")
    print("")
    print("Your word have " + length + " letters! Good luck!")
    print("")

    while a <= 5:
        guess = input("Enter letter: " + dot1 + " > ")
        upper = guess.upper()

        if dot == storelist:
            Maxguess = True
            break

        if a == 5:
            Maxguess = False
            break
        
        if guess in guessList and guess in storelist:
            print("Hey! You already guess " + guess + " correctly!")
            print("")
        elif guess in guessList and guess not in storelist:
            print("Hey! You already guess " + guess + " incorrectly!")
            print("")

        else:
            if upper in ml or guess in ml:
                print("")
            elif guess not in ml or upper not in ml:
                a += 1
                print("Too bad! "+ guess + " is not in the word")
                print("")

        guessList.append(guess)

        for i in range(0, len(ml)):
            if(dot != storelist):
                if(guess == storelist[i] or upper == storelist[i]):
                    del(dot[i])
                    dot.insert(i, storelist[i])
                    dot1 = " ".join(dot)
                    Maxguess = False

            elif dot == storelist:
                Maxguess = True
                break

    if(Maxguess == False):
        print("")
        print("Boo! You lost!")
        print("")

    elif Maxguess == True:
        print("")
        print("You won!")
        print("")
        

    getoption()
        
# Main program
getstart()