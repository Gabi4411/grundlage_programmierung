# from Wurfel import Die
# from frac import Frac
# from auto import Auto
# from statistics import Statistics
from konto import Konto


def main():
    # d = Die(6)
    # roll = d.roll()
    # while roll != 6:
    #     print(f'rolled: {roll}')
    #     roll = d.roll()
    # print(f'rolled: {roll}')
    #
    # f1 = Frac(4, 12)
    # f1.reduce()
    # print(f'{f1.n}/{f1.m}')
    #
    # s = Statistics()
    # autos = [
    #     Auto('m1', 'm2', 800, 'red'),
    #     Auto('m1', 'm2', 1000, 'blue'),
    #     Auto('m1', 'm2', 900, 'red')
    # ]
    #
    # color = 'red'
    # print(s.count_color(autos, color))
    #
    # print(s.avg_year(autos, "m1"))
    balanta = Konto('123', 'eu')
    balanta.plus(20)
    balanta.minus(10)
    balanta.plus(50)
    print(balanta.betrag)


main()
