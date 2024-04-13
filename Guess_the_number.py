import random
target = random.randint(0,1000)

while True:
    userChoice = input("Guess the Target or Quit: ")
    if (userChoice == "QUIT"):
        break

    userChoice = int(userChoice)
    if (userChoice == target):
        print("success : Correct Guess !!")
        break
    elif (userChoice < target):
        print("Your number was to small , Take a Bigger Guess....")
    else:
        print("Your number was too big , Take a Smaller Guess....")

print("------GAME OVER------")
