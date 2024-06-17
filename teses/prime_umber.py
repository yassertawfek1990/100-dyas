number = int(input("type a number\n"))

def prime_number(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        print(f" the number {n} is a Prime number")
    else:
        print(f" the number {n} is not a Prime number")

prime_number(number)