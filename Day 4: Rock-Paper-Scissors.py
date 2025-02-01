import random
rock=( ''' 
  _______
---'   (____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
scissors=('''    
 _______
---'   ____)
________________
          ______)
       __________)
      (____)
---.__(___)
''')
paper=('''     
_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
game=[rock, paper, scissors]
ip= int(input("What would you use? press 0 for rock, 1 for paper and 2 for scissors\n you chose:\n"))

cip=random.randint(0,2)

print("You chose\n")
print(game[ip])
print("Computer chose\n")
print(game[cip])

if ip==cip:
    print("The Result is a draw")
elif ip==0 & cip==2:
    print("You win!")
elif ip==2 & cip==0:
    print("The Computer wins!")
elif ip>cip:
    print("You win!")
elif cip>ip:
    print("The Computer wins!")
else:
    print("Choose a valid input between 0 and 2")
