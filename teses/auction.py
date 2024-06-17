import os

def clear_terminal():
    # ANSI escape code to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the terminal
clear_terminal()

dic = {}

more = "yes"
while more == "yes":
    name = input("type your name\n")
    bid = int(input("type your bid:$ "))
    dic[name] = bid
    more = input("if you want to add more type yes\n")
    clear_terminal()

import operator
high = max(dic.items(), key=operator.itemgetter(1))[0]

print(f"the person with highest bid is {high} with bid {dic[high]}")

keys = []
values = []
for key, value in dic.items():
    keys.append(key)
    values.append(value)
biggest_value = max(values)
highest_name = keys[values.index(biggest_value)]

print(f"the person with highest bid is {highest_name} with bid {biggest_value}")
