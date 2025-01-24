word_list=["Life","Death","Pessimist", "Suicide", "Allah", "Chicken", "Time", "Philosophy", "Sin", "Punishment"]


import random
chosen_word=random.choice(word_list).lower()
print(chosen_word)
lives=6
clist=[]
game_over= False

while not game_over:
    display=""
    letter=input("Enter a letter: ")


    for i in chosen_word:
        clist.append(i)
        if i == letter:
             display += i
        elif i in clist:
             display+=i
             print("You've already guessed the letter")
        else:
             display += "_"
    if letter not in chosen_word:
        lives-=1
    print(display.lower())
    print("You have "+ str(lives)+ " lives left")

    if "_" not in display:
        game_over=True
        print("You Win")
    elif lives==0:
        game_over=True
        print("You Lose")
