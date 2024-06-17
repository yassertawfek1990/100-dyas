final_word = "elephant"

guess = input("right your guess!\n")

if guess in final_word:
    for i in final_word:
        if i == guess:
            print(i)
        else:
            print("-")