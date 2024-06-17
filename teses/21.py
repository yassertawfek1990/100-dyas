import random
def ace(krot):       
    if sum(krot) > 21:
        if 11 in krot:
            score = sum(krot) - 10
        else:
            score = sum(krot)
    else:
        score = sum(krot)
    return score

def withdraw(dick,krot,n):
    s = random.sample(dick,n)
    krot += s
    return krot

def remove(dick,krot,n):
    n += 1 
    for x in range(-1, -n, -1):
        dick.pop(dick.index(krot[x]))
    return dick
# more = input("do you want to play a game of black jack type 'y' or 'n': ")
# print(f"Your cards: {cards}, current score: {your_score}")
# print(f'Computers first card: {cp_cards}')
# another = input("type'y' to get another card, type'n' to pass:")
# print(f"Your cards: {cards}, current score: {your_score}")
# print(f"Your final hand: {cards}, final score: {your_score}")
# print(f"Computer's final hand: {cp_cards}, final score: {cp_score}")
# print("You went over. You lose 😭")

the_dick = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]
the_cards = []
the_cpcards = []
# cards = random.sample(dick,2)
# print(cards)
# dick.pop(dick.index(cards[0]))
# dick.pop(dick.index(cards[1]))
# print(dick)
# cp_cards = random.sample(dick,1)
# print(cp_cards)
# more = input("do you want to play a game of black jack type 'y' or 'n': ")
# while more == "y":
def game21(dick,cards,cp_cards):
    cards = withdraw(dick, cards,2)
    dick = remove(dick, cards,2)
    your_score = sum(cards)
    print(f"Your cards: {cards}, current score: {your_score}")
    cp_cards = withdraw(dick, cp_cards,1)
    dick = remove(dick, cp_cards,1)
    print(f'Computers first card: {cp_cards}')
    another = input("type'y' to get another card, type'n' to pass:")
    if another == "y":
        cards = withdraw(dick, cards,1)
        dick = remove(dick, cards,1)
        print(len(dick))
        your_score = sum(cards)
        print(f"Your cards: {cards}, current score: {your_score}")
        print(f'Computers first card: {cp_cards}')
        cp_cards = withdraw(dick, cp_cards,1)
        dick = remove(dick, cp_cards,1)
        if sum(cp_cards) < 15:
            cp_cards = withdraw(dick, cp_cards,1)
            dick = remove(dick, cp_cards,1)
        cp_score = ace(cp_cards)
        your_score = ace(cards)
        print(f"Your final hand: {cards}, final score: {your_score}")
        print(f"Computer's final hand: {cp_cards}, final score: {cp_score}")
        if your_score == 21 and cp_score == 21:
            print("its a drwa")
        elif your_score == 21 and cp_score != 21:
            print("you win")
        elif your_score < 21 and cp_score > 21:
            print("you win")
        elif your_score != 21 and cp_score == 21:
            print("you loose")
        elif your_score < 21 and your_score > cp_score:
            print("you win")
        elif your_score < 21 and your_score == cp_score:
            print("its a drwa")
        else:
            print("you loose") 
    if another == "n":
        cp_cards = withdraw(dick, cp_cards, 1)
        dick = remove(dick, cp_cards,1)
        if sum(cp_cards) < 15:
            cp_cards = withdraw(dick, cp_cards,1)
            dick = remove(dick, cp_cards,1)
        cp_score = ace(cp_cards)
        your_score = ace(cards)
        print(f"Your final hand: {cards}, final score: {your_score}")
        print(f"Computer's final hand: {cp_cards}, final score: {cp_score}")
        if your_score == 21 and cp_score == 21:
            print("its a drwa")
        elif your_score == 21 and cp_score != 21:
            print("you win")
        elif your_score < 21 and cp_score > 21:
            print("you win")
        elif your_score != 21 and cp_score == 21:
            print("you loose")
        elif your_score < 21 and your_score > cp_score:
            print("you win")
        elif your_score < 21 and your_score == cp_score:
            print("its a drwa")
        else:
            print("you loose")

    more = input("do you want to play a game of black jack type 'y' or 'n': ")
    if more == "y":
        the_dick = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]
        the_cards = []
        the_cpcards = []
        game21(the_dick,the_cards,the_cpcards)
    else:
        print("Goodbye")
        
more = input("do you want to play a game of black jack type 'y' or 'n': ")
if more == "y":
    game21(the_dick,the_cards,the_cpcards)
else:
        print("Goodbye")


            




