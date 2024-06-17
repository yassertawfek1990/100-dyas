
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = ["quarters", "dimes","nickles","pennies"]
each_coin = []

money = {"q": .25, "d": .1, "n": .05, "p": 0.01}

def pay(money,each_coin):
    total = 0
    ind = 0
    for key, value in money.items():
        total += value * each_coin[ind]
        ind += 1
    return total

def choice(menu,x):
    return menu[x]

def coffee(x, resources, start):
    change = 0
    global profit
    global success
    global money
    global coins

    for a,b in x["ingredients"].items():
        if b <= resources[a]:
              resources[a] -= b
        else:
            print(f"Sorry there is not enough {a}.")
            return
    print("Please insert coins." )
    each_coin = []
    for i in coins:
        each_coin.append(int(input(f"how many {i}?:")))
    paid = pay(money,each_coin)

    if paid >= x["cost"]:
        change = round(paid - x["cost"],2)
        profit += paid
        print(f"Here is ${change} in change.")

    else:
        print("Sorry that's not enough money. Money refunded.")
        for a,b in x["ingredients"].items():
              resources[a] += b
        return
    print(f"Here is your {start} ☕️. Enjoy!")
    return

def go():
    global menu
    global resources
    global profit

    success = False
    start = input("wWhat would you like? (espresso/latte/cappuccino):")
    if start == "off":
        print("Goodbye")
        return
    if start == "report":
        for a,b in resources.items():
            if a != "coffee":
                print(a,b,"ml")
            else:
                print(a,b,"gm")
        print(f"Profit: {round(profit,2)}$")
        go()
    cof = choice(menu,start)
    coffee(cof, resources,start)
    if success:
        print(f"Here is your {start} ☕️. Enjoy!")
    go()

go()