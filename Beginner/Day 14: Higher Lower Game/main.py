import game_data
import random
import art


A=random.choice(game_data.data)
B=random.choice(game_data.data)
if A==B:
    B=random.choice(game_data.data)
score=0
answer=True
while answer:
    print(art.logo)
    print(f"Compare {A["name"]}, {A["profession"]}, from {A["place_of_birth"]}")
    print(art.vs)
    print(f"Against {B["name"]}, {B["profession"]}, from {B["place_of_birth"]} \n")
    choice=(input("Who has more followers: A or B?"))

    if (choice=='A'and A["followers"]>B["followers"]) or (choice=='B' and B["followers"]>A["followers"]) :
            print("You guessed correctly!")
            score+=1
            print(f"Your Score is: {score}" )
            print("\n" * 200)
    elif (choice=='A'and B["followers"]>=A["followers"]) or (choice=='B' and A["followers"]>=B["followers"]) :
        print("Oh No! You're Answer was wrong")
        print(f"Your final score is {score}")
        answer=False
    else:
        print("Please give an appropriate response: A or B")
        exit()
    A = B
    B = random.choice(game_data.data)
