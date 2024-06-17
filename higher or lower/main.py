from menus import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
c = CoffeeMaker()
f = MoneyMachine()
def go():
    start = input(f"wWhat would you like? {m.get_items()}:")
    
    if start == "off":
        print("Goodbye")
        return
    elif start == "report":
        c.report()
        f.report()
    else:
        i = m.find_drink(start)
        if c.is_resource_sufficient(i):
            if f.make_payment(i.cost):
                c.make_coffee(i)
            else:
                go()
        else:
            go()

    go()

go()