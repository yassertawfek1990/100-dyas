import os

def clear_terminal():
    # ANSI escape code to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the terminal


# n1 = float(input('what is the first number?: '))
# op = input('+\n-\n*\n/\nPick an operation: ')
# n2 = float(input('what is the second number?: '))
# more = input(f'Type "y" to continue calculating with {final} or type "n" to start a new calculation:')
# print(n1+n2)

        

def add(n1,n2):
    return n1 + n2
def div(n1,n2):
    return n1 / n2
def mul(n1,n2):
    return n1 * n2
def sub(n1,n2):
    return n1 - n2

ch = {"+": add,"-": sub,"*": mul ,"/": div }
def calc(n1,n2,op):
    if op == "+":
        t = add(n1,n2)
    elif op == "-":
        t = sub(n1,n2)
    elif op == "/":
        t = div(n1,n2)
    elif op == "*":
        t = mul(n1,n2)
    return t


def calculator():
    n1 = float(input('what is the first number?: '))
    more = "y"
    while more == "y": 
        op = input('+\n-\n*\n/\nPick an operation: ')
        n2 = float(input('what is the second number?: '))
        final = ch[op](n1,n2)
        print(f"{n1}{op}{n2}={final}")
        more = input(f'Type "y" to continue calculating with {final} or type "n" to start a new calculation:')
        if more == "y":
            n1 = final
        else:
            more = "n"
            clear_terminal()
            calculator()

calculator()