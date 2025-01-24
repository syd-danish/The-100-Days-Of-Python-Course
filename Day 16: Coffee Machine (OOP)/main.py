from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffiz=CoffeeMaker()
mm=MoneyMachine()




on_or_off=True
while on_or_off:
    choose = (input(f"What would you like?\n{menu.get_items()}Report\nOFF\n"))
    if choose == "Report":
        coffiz.report()
        mm.report()
    elif choose == "OFF":
        on_or_off=False
    else:
        drink = menu.find_drink(choose)
        if coffiz.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            coffiz.make_coffee(drink)
