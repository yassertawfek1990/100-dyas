alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


repeat = "yes"

def cipher(message, shift, task):
    new = ""
    shift = shift % 26
    if task == 'decode':
        shift *= -1
    for i in message:
        if i in alphabet:
            position = alphabet.index(i)
            new += alphabet[position + shift]
        else:
            new += i
    print(f"here is the {task} result: {new}")


while repeat == "yes":
    task = input("type 'encode' to encrypt or 'decode' to decrypt\n")
    while task not in ["encode", "decode"] :
       task = input(("wrong input please try again\ntype 'encode' to encrypt or 'decode' to decrypt\n"))
    message = (input("type your message\n")).lower()
    shift = int(input("type the shift number\n"))
    cipher(message, shift, task)
    repeat = input("type 'yes' if you want to go agian or 'no' if you want to stop\n")

print("Goodbye")
    