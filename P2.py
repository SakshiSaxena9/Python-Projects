import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess : "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
            
print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken a highscore")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))