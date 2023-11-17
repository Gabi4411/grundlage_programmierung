from repository.director import *


def deseneaza():
    sterge()
    opt = input("Scrie un cuvant: ")
    opt = opt.upper()
    for litere in opt:
        letters[litere]()
