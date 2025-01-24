import random

print("Welcome to the Number Guessing Game!")
number= random.randint(1,100)
print("I am thinking of a number between 1 and 100.")
diff=int(input("Choose a Difficulty\nType 1 for Easy\nType 2 for Hard\n"))
if diff==1:
    lives=10
elif diff==2:
    lives=5
else:
    exit()
while lives>0:
    guess=int(input("Make A Guess\n"))
    if guess>100 or guess<0:
        print("GUESS THE NUMBER INSIDE THE GIVEN RANGE! YOU ACTUAL DUMBFUCK!")
        exit()
    if guess==number:
        print("Congratulations you've correctly guessed the number!")
        exit()
    else:
        if guess>number:
            print("Uh Huh! You've guessed too high! ")
        elif number>guess:
            print("Uh Huh! You've guessed too low! ")
        lives-=1
        print(f"You have {lives} lives left!")
