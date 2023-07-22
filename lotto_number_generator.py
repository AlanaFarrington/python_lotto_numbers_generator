import random

Lotto_number_list = []

def lotto_generator():
    Lotto_number_list = []
    for lotto_number in range(6):
        Lotto_number_list.append(random.randint(1,50))
    print(Lotto_number_list)

def multiple_lotto_generator(rows):
    for row in range(rows):
        lotto_generator()

rows = input('How many sets of lottery numbers do you want? ')

multiple_lotto_generator(int(rows))