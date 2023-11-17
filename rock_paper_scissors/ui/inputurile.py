import random


def utilizatorul():
    while True:
        user = input("Piatra, foarfeca sau hartie? Alege: ").lower().strip()
        if user in ('piatra', 'foarfeca', 'hartie'):
            return user
        else:
            print('Nu exista varianta asta mai incearca!')


def computer():
    alegeri = ['piatra', 'foarfeca', 'hartie']
    pc = random.choice(alegeri)
    return pc
