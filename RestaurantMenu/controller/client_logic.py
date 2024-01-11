from repository.clientrepo import ClientRepo
from modelle.client import Client
from .datarepo_logic import showdata
from repository.orderrepo import OrderRepo


clientmanager = ClientRepo('clients.dat')
ordermanager = OrderRepo('orders.dat')


def showclients():
    print("Clients: ")
    showdata(2)


def addclient():
    name = input("Name of the client: ")
    adress = input("Address of the client: ")

    clients: list = clientmanager.load() if clientmanager.load() else []
    client = Client(1, name, adress)
    clients.append(client)
    clientmanager.sort(clients)


def updateclients():
    showclients()
    idlist = int(input("The id of the item you want to update: "))
    clients: list = clientmanager.load()

    idp = clients[idlist].idp
    name = input("Enter the new name: ")
    adress = input("Enter the new adress: ")
    client = Client(idp, name, adress)
    clientmanager.update(idlist, client)


def deleteclient():
    showclients()
    idp = int(input("The id of the item you want to delete: "))
    clientmanager.remove(idp)
    ordermanager.remove(idp)
