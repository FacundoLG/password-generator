import random
import string
lower_letters = string.ascii_lowercase
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

def generate_password():
    part1 = generate_letters(10)    
    print(part1)

def run():
    generate_password()

if __name__ == "__main__":
    run()