import time
import random

def displayIntro():
    print("You are in a land full of dragons, in front of you,")
    print("you see two caves. In one cave, the dragon is friendly")
    print("and will share its treasure with you. The other dragon")
    print("is greedy and hungry and will eat you on sight.")

def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you, he opens his jaws and...")
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    
    if chosenCave == str(friendlyCave):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite")

playAgain = "yes"

displayIntro()
print("Pick a cave, 1 or 2")
chosenCave = input()
checkCave(chosenCave)

while playAgain.lower() == "yes" or playAgain.lower() == "y":
    print("Would you like to play again?")
    playAgain = input()
    if playAgain.lower() == "yes" or playAgain.lower() == "y":
        break
    displayIntro()
    print("Pick a cave, 1 or 2")
    chosenCave = input()
    checkCave(chosenCave)