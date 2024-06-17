
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
if dif == "easy":
    trials = 10
elif dif == "hard":
    trials = 5
n = random.choice(range(101))
print(f"You have {trials} attempts remaining to guess the number.")
n = random.randint(1,100)

def guess():
    global trials
    g = int(input("Make a guess: "))
    if g == n:
        print(f"You got it! The answer was {n}.")
        trials = 0
    elif g < n:
        print("Too low.")
        trials -= 1
    elif g > n:
        print("Too high.")
        trials -= 1
    if g != n and trials == 0:
        print("You've run out of guesses, you lose.")
        print(f"the number is {n}")

    return trials

while trials > 0:
    trials = guess()
    if trials != 0:
        print("Guess again.")
        print(f"You have {trials} attempts remaining to guess the number.")




    






