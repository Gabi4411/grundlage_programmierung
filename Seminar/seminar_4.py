from math import gcd


def simplify(frac):
    g = gcd(frac[0], frac[1])

    return frac[0]//g, frac[1]//g


def add(a, b):
    return simplify((a[0] * b[1] + b[0] * a[1], a[1] * b[1]))


def sub(a, b):
    return simplify((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))


def mul(a, b):
    return a[0] * b[0], a[1] * b[1]


def div(a, b):
    return a[0] * b[1], a[1] * b[0]


def add_frac(fracs, frac):
    fracs.append(frac)


def sum_fracs(fracs):
    suma = 0, 1

    for frac in fracs:
        suma = add(suma, frac)

    return suma


def loschen(fracs, nr):
    if nr > len(fracs) - 1:
        exit('Index to big')
    else:
        del fracs[nr]
        return fracs


def test_add():
    assert add((1, 2), (2, 3)) == (7, 6)


def menu():
    return """
        1 - add frac
        2 - calculate sum
        3 - delete element
        4 - exit
    """


def main():

    fracs = []

    while True:
        print(menu())

        opt = int(input('opt = '))

        if opt == 1:
            n = int(input('n = '))
            m = int(input('m = '))

            add_frac(fracs, (n, m))

        if opt == 2:
            n, m = sum_fracs(fracs)
            print('sum =', (n, m))

        if opt == 3:
            nr = int(input('nr = '))
            loschen(fracs, nr)
            print(fracs)

        if opt == 4:
            break


main()
