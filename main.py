import sys
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
options=menu.get_items()
is_on=True
while is_on :
 choice=input(f"What would you like {options}").lower().strip()
 if choice=="off":
   sys.exit()
 drink=menu.find_drink(choice)


 if coffee_maker.is_resource_sufficient(drink):
  money=money_machine.process_coins()
 
  if money_machine.make_payment(money):
     
     coffee_maker.make_coffee(drink)
 else :
  print("Sorry the resources are not sufficient ")
  print(coffee_maker.report())
