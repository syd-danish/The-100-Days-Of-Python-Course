ingredients={"Water(ml)": 300, "Coffee(g)":100, "Milk(ml)":200}

Coffee_Options={
    1 :{"product_name":"Espresso","cost":1.5, "ingredients": {"Water(ml)": 50, "Coffee(g)":18, "Milk(ml)":0}},
    2 :{"product_name":"Latte","cost":2.5, "ingredients": {"Water(ml)": 200, "Coffee(g)":24, "Milk(ml)":150}},
    3 :{"product_name":"Cappuccino","cost":2.5,"ingredients": {"Water(ml)": 250, "Coffee(g)":24, "Milk(ml)":100}}
}


Water=300
Milk=200
Coffee=100
Total=0

def money_spot():
    global Total
    penny = int(input("How many Pennies would you like to enter?"))* 0.01
    nickel = int(input("How many Nickels would you like to enter?"))* 0.05
    dime = int(input("How many Dimes would you like to enter?"))*.1
    quarter = int(input("How many Quarters would you like to enter?"))* .25
    Total += penny + nickel + dime + quarter
    return Total.__float__()



while True:
    choice = int(input("What would you like?\nPress 1 for an Espresso\nPress 2 for a Latte\nPress 3 for a Cappucino\nPress 4 to check remaining content\nPress 5 for exit\n"))
    if choice == 4:
        print(f"{Water}ml of water\n{Coffee}g of coffee\n{Milk}ml of milk")
    elif choice==5:
        exit()
    elif choice in (1, 2, 3):

        if money_spot() < Coffee_Options[choice]["cost"]:
            print("Sorry you dont have enough money.")
            
        if Coffee_Options[choice]["ingredients"]["Water(ml)"] > Water:
            print("Sorry for the inconvenience, The Machine does not have enough water!")
        elif Coffee_Options[choice]["ingredients"]["Coffee(g)"] > Coffee:
            print("Sorry for the inconvenience, The Machine does not have enough coffee! ")
        elif Coffee_Options[choice]["ingredients"]["Milk(ml)"] > Milk:
            print("Sorry for the inconvenience, The Machine does not have enough milk!")
        else:
            Water -= Coffee_Options[choice]["ingredients"]["Water(ml)"]
            Milk -= Coffee_Options[choice]["ingredients"]["Milk(ml)"]
            Coffee -= Coffee_Options[choice]["ingredients"]["Coffee(g)"]
            Total -= Coffee_Options[choice]["cost"]
            print(f"Here is your {Coffee_Options[choice]["product_name"]}")
            print(f"Your change is {round(Total, 2)}")

