import random

secreteNumber = random.randint(1, 100)
print("i am thinking a number between 1 to 100")
for guessTaken in range(1, 10):
    print("take a guess")
    guess = int(input())
    if guess < secreteNumber:
        print("your guess is too low")
    elif guess > secreteNumber:
        print("your guess is too high")
    else:
        break

if guess == secreteNumber:
    print(f"good job!you guessed my number in {guessTaken} guesses!")
else:
    print(f"Nope! the number i was thinking of was {secreteNumber} ")
