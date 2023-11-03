import math


def kgv_finden(a, b):
    return a * b // math.gcd(a, b)

def entfernen(l):
    new_l = []

    for i in range(len(l)):
        if l[i] not in new_l:
            new_l.append(l[i])

    return new_l


def inversul_numarului(nr):
    x = 0
    p = 1

    while nr != 0:
        x = x * p + nr % 10
        nr //= 10
        p *= 10

    return x


def symmetrischen_paaren(l):
    anz = 0
    i = 0
    while i < len(l):
        for j in range(i + 1, len(l)):
            if l[i] == inversul_numarului(l[j]):
                anz += 1
        i += 1

    return anz


def konkatenation(l):
    string = ''
    l.sort(reverse = True)

    for i in range(len(l)):
        string += str(l[i])

    return int(string)


def verschlusseln(l):
    new_l = []
    x = l[0]

    for i in range(len(l)):
        new_l.append(l[i] + x)

    return new_l


def filtern(l, formel):
    new_l = []

    for i in l:
        x = i // 10
        y = i % 10
        if eval(formel) == True:
            new_l.append(i)
    return new_l

def make_all_a_list(l):
    new_l = []

    for i in l:
        new_l.append(i // 10)
        new_l.append(i % 10)

    return new_l


def domino(l):
    anz = 0
    max = 0
    i = 1

    while i < (len(l) - 1):
        if i % 2 == 0:
            i += 1
        else:
            if l[i] == l[i + 1]:
                anz += 1
            elif anz > max:
                max = anz
                anz = 0
            i += 1

    return max


def kgv_von_liste(l, index_from, index_to):
    kgv = l[index_from]

    for i in range(index_from + 1, index_to + 1):
        kgv = kgv_finden(kgv, l[i])

    return kgv


def main():
    # print(entfernen(lista))
    # print(symmetrischen_paaren(lista))
    # print(konkatenation(lista))
    # print(verschlusseln(lista))
    # print(filtern(lista, 'x/y==2'))
    lista = [12, 24, 48, 45, 56, 68, 82, 22, 45, 64, 46, 42, 23]
    print(domino(make_all_a_list(lista)))
    print(kgv_von_liste(lista, 0, 2))

main()
