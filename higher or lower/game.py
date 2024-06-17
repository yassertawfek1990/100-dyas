from data import datas
from art import logo, vs
import random
import os

def clear_terminal():
    # ANSI escape code to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


print(logo)
random.shuffle(datas)
more = True
n = 0
b = 1
score = 0
while more:   
    clear_terminal()
    print(logo)
    if score > 0:
        print(f"You are right, your score is {score}")
    print(f"Compare A: {datas[n]["name"]}, {datas[n]["description"]}, {datas[n]["country"]}")
    print(vs)
    print(f"against B: {datas[b]["name"]}, {datas[b]["description"]}, {datas[b]["country"]}")
    win = (input("Who has more followers? Type 'A' or 'B':")).upper()
    if win == "A":
        if datas[n]["follower_count"] > datas[b]["follower_count"]:
            score +=1
            print(f"You are right, your score is {score}")
            if n > b :
                b = n + 1
            elif b > n :
                b = b + 1 
        else:
            clear_terminal()
            print(logo)
            print(f"Sorry, that's wrong. Final {score}:")
            more = False
    elif win == "B":
        if datas[b]["follower_count"] > datas[n]["follower_count"]:
            score += 1
            print(f"You are right, your score is {score}")
            if n > b :
                n = n + 1
            elif b > n :
                n = b + 1 
        else:
            clear_terminal()
            print(logo)
            print(f"Sorry, that's wrong. Final {score}:")
            more = False
    else:
        clear_terminal()
        print(logo)
        print(f"Sorry, that's wrong. Final {score}:")
        more = False