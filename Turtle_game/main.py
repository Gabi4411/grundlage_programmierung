from ui.console import menu
from logik.game import deseneaza
from draw.desen import deseneaza_din_taste

def run():
    with open('textul.txt', 'a') as fisier:
        fisier.write('\n')

    while True:
        print(menu())
        inp = int(input("Alege o optiune: "))

        if inp == 1:
            deseneaza()
        if inp == 2:
            deseneaza_din_taste()
        if inp == 0:
            break


run()
