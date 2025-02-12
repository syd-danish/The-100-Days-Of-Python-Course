import random
from random import shuffle

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['=','+','-','#','$',':',';','*','%','[',']','!','{','}']
numbers=['1','2', '3','4','5','6','7','8','9', '0']


print("Welcome to PyPassword Generator!")
no_letters= int(input("How many letters would you like to generate in your password?\n "))
no_symbols=int(input("How many symbols would you like to generate in your password? \n"))
no_numbers=int(input("How many numbers would you like to generate in your password? \n"))
list=[]
for i in range(0, no_letters):
    list.append(random.choice(letters))
for i in range(0,no_symbols):
    list.append(random.choice(symbols))
for i in range(0,no_numbers):
    list.append(random.choice(numbers))

shuffle(list)
password=""
print(list)
for i in list:
    password+=i
print(password)
