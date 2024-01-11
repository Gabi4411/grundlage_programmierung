from repository.orderrepo import OrderRepo
from repository.clientrepo import ClientRepo
from .menu_logic import showmenu, drinkmanager, cookeddishmanager
from .client_logic import addclient
from .datarepo_logic import showdata
from modelle.order import Order


ordermanager = OrderRepo('orders.dat')
clientmanager = ClientRepo('clients.dat')


def searchclientname():
    name = input("What client are you searching for: ")
    clients = clientmanager.load() if clientmanager.load() else []
    print('\n')
    ids = []
    if clients:
        print("Client: ", '\n')
        for idx in range(len(clients)):
            if name.lower() in clients[idx].name.lower():
                print(idx, str(clients[idx]))
                ids.append(clients[idx].id)


def searchbyaddress():
    address = input("What address are you searching for: ")
    clients = clientmanager.load() if clientmanager.load() else []
    print('\n')
    # ids = []
    if clients:
        print("Client: ", '\n')
        for idx in range(len(clients)):
            if address.lower() in clients[idx].address.lower():
                print(idx, str(clients[idx]))


def addclientsorder():
    print('\n', "Clients: ")
    showdata(2)
    addclient()


def neworder():
    value = int(input("Enter the id of the client that orders: "))
    showdata(2)
    clients = clientmanager.load()
    client = clients[value]

    cookeddishesids = []
    drinksids = []
    cookeddishes = cookeddishmanager.load() if cookeddishmanager.load() else []
    drinks = drinkmanager.load() if drinkmanager.load() else []

    showmenu()

    while True:
        choose = int(input("""
        What item do you want to add:
        1 - Select a cooked dish
        2 - Select a drink
        0 - Exit
        
        """))

        if choose == 0:
            break

        if choose == 1:
            idp = int(input("Id: "))
            if idp < len(cookeddishes):
                cookeddishesids.append(cookeddishes[idp].idp)
            else:
                print("Not found")
        else:
            idp = int(input("Id: "))
            if idp < len(drinks):
                drinksids.append(drinks[idp].idp)
            else:
                print("Not found")

    order = Order(1, client.idp, cookeddishesids, drinksids)
    orders = ordermanager.load() if ordermanager.load() else []
    orders.append(order)
    ordermanager.sort(orders)

    Order.printreceipt()


def showorders():
    print("Orders: ", '\n')
    showdata(3)

    orders = ordermanager.load()
    value = int(input("Show the receipt of which order you want: "))
    orders[value].printreceipt()
