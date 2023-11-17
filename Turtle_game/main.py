from ui.console import menu, varianta_2
from logik.game import deseneaza
from draw.desen import deseneaza_din_taste
from repository.director import sterge_pt_2


def run():
    with open('textul.txt', 'a') as fisier:
        fisier.write('\n')

    while True:
        print(menu())
        inp = int(input("Alege o optiune: "))

        if inp == 1:
            deseneaza()
        if inp == 2:
            sterge_pt_2()
            print(varianta_2())
            deseneaza_din_taste()
        if inp == 0:
            break


run()
