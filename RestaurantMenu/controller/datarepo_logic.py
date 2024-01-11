from repository.clientrepo import ClientRepo
from repository.drinkrepo import DrinkRepo
from repository.cookeddishrepo import CookedDishRepo
from repository.orderrepo import OrderRepo


def showdata(nr):
    types = {
        0: CookedDishRepo('cookeddish.dat'),
        1: DrinkRepo('drink.dat'),
        2: ClientRepo('clients.dat'),
        3: OrderRepo('orders.dat')
    }

    repo = types[nr]

    lista = repo.load()
    if lista:
        for idx in range(len(lista)):
            print(f"{idx}, {str(lista[idx])}")

    print('\n')
