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

def generate_number(max_value: int = 10000):
    return str(random.randint(0,max_value))
def random_symbol():
    return symbols[random.randint(0, len(symbols) - 1)]

def generate_password():
    part1 = generate_letters(10)    
    symbol = random_symbol()    
    part2 = generate_number(1000000000)
    symbol2 = random_symbol()
    part3 = generate_letters(20)
    print(part1 +symbol+ part2+ symbol2+ part3)

def run():
    generate_password()

if __name__ == "__main__":
    run()