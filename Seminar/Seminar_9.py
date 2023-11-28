# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, w):
#         print(f'{self.name} manca {w}.')
#
#
# class Pig(Animal):
#     def __init__(self, name, age):
#         Animal.__init__(self, name)
#         self.age = age
#
#     def sleep(self):
#         print(f'{self.name} motaie.')
#
#
# class Chicken(Animal):
#     def __init__(self, name, color):
#         Animal.__init__(self, name)
#         self.color = color
#
#
# class Farm:
#     def __init__(self, name, city, animals=[]):
#         self.name = name
#         self.city = city
#         self.animals = animals
#
#     def feed_animals(self, food):
#         for animal in self.animals:
#             animal.eat(food)
#
#
# def main():
#     bob = Animal('Bob')
#     bob.eat('plante')
#
#     zob = Pig('Zob', 2)
#     zob.eat('lucerna')
#
#     lob = Chicken('Lob', 'black')
#     lob.eat('porumb')
#
#     f = Farm('Ferma Verde', 'Cluj', [bob, zob, lob])
#     f.feed_animals('plants')
#
#
# main()
#
#
class Raum:
    def __init__(self, nr, seats):
        self.nr = nr
        self.seats = seats

    def __str__(self):
        return f'Raum: nr = {self.nr}, seats = {self.seats}'

    def __eq__(self, other):
        return self.nr == other.nr


class Lab(Raum):
    def __init__(self, nr, seats, os):
        Raum.__init__(self, nr, seats)
        if os not in ['unix', 'linux', 'windows']:
            raise AttributeError('os not allowed...')

        self.os = os

    def __str__(self):
        return f'Lab: nr = {self.nr}, seats = {self.seats}, os = {self.os}'


class Building:
    def __init__(self, rooms):
        self.rooms = rooms

    def seats(self):
        for room in self.rooms:
            print(room.seats)


def main():
    r1 = Raum('21A', 100)
    r2 = Raum('21B', 100)
    l1 = Lab('01A', 20, 'windows')
    print(r1)
    print(r1 == r2)
    print(l1)
    b = Building((r1, r2, l1))
    b.seats()


main()
