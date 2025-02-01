print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************\n''')

print("Welcome to Treasure Island!\n")
print("Your mission is to find the treasure!\n")
cross_road= input("You are at a crossroad, type R to go right or type L to go left\n")


if cross_road=="R":
    lake = input("You've come to a lake, there is an island in the middle of the lake, "
                 "will you wait for a boat or swim?\n press W for wait and S for swim")
    if lake=="W":
        door = input("You have now traversed the whole island and have ended up finding 3 doors\n"
                     "a red, a blue and a yellow door, which one do you choose? Y, B or R\n")
        if door=="R":
            print("Congratulations, You have found the treasure!")
        elif door=="B" or door=="Y":
            print("You choose the wrong door! GameOver!")
        else:
            print("Enter a Valid Input(Y, B or R)\n")

    elif lake=="S":
        print("You drowned while swimming in the lake! GameOver!")
    else:
        print("Enter a Valid Input (W or S)\n")
elif cross_road=="L":
    print("You went to the wrong way! GameOver!")
else:
    print("Enter a valid input (R or L)\n")
