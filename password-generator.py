import numbers
import random
import string

lower_letters = string.ascii_lowercase
symbols = string.punctuation

def generate_letters(length: int):
    letters = ""
    
    for _ in range(length):
        random_index = random.randint(0, len(lower_letters) - 1)
        
        want_upper = random.randint(0,1)
        if want_upper == 0:
            letters += lower_letters[random_index]
        else:
            letters += lower_letters[random_index].upper()
    
    return letters

def generate_number(max_length: int = 10000):
    number = ""
    for _ in range(0, max_length):
        number += str(random.randint(0,9))
    return number


def random_symbol():
    return symbols[random.randint(0, len(symbols) - 1)]

def generate_password(structure: str = None,max_length: int = None):
    password = ""
    if not structure: structure = input("Write an structure eg<L-N-L-N> : ") 
    try:
        max_length = int(input("Max length:"))
    except ValueError:
        print("Write a number")
        generate_password(structure,max_length)
    print(max_length)

    for char in structure:
        if char == "N":
            password += generate_number(max_length)
        elif char == "L":
            password += generate_letters(max_length)
        elif char == "-":
            password += random_symbol()
        else:
            print("Only N(numbers)S(symbol)L(letters) and - chars are allowed eg<N-S-L-L")
            return generate_password(structure,max_length)
    if len(password) < 1:
        print("You need a custom structure")
        return generate_password(structure,max_length)

    return password

def run():
    user_input = input("Write a name for your password: ")
    generated_password = generate_password()
    print(generated_password)

if __name__ == "__main__":
    run()