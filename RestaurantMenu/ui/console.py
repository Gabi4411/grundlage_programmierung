from controller.menu_logic import showmenu, adddrink, addcookeddish, search, showupdatedmenu, showmenuafterdelete
from controller.client_logic import showclients, addclient, deleteclient, updateclients
from controller.orders_logic import showorders, searchbyaddress, searchclientname, neworder, addclientsorder


def console():
    choose = {
        1: menuconsole,
        2: clientconsole,
        3: orderconsole
    }

    while True:
        print("""
        1 - Menu
        2 - Clients
        3 - Orders
        0 - Exit
        
        """)
        option = int(input("Choose an option: "))
        if option == 0:
            exit()

        choose[option]()


def dishtype():
    value = int(input("""
    Choose the type of dish you want to add:
        1 - Cooked Dish
        2 - Drink
        
    """))

    options = {
        1: addcookeddish,
        2: adddrink
    }

    options[value]()
    print("Item added successfully!")
    menuconsole()


def menuconsole():
    while True:
        value = int(input(""" 
        1 - Menu
        2 - Item search
        3 - Add a new item 
        4 - Update an item
        5 - Delete an item
        0 - Back
        
        """))

        options = {
            1: showmenu,
            2: search,
            3: dishtype,
            4: showupdatedmenu,
            5: showmenuafterdelete,
            0: console
        }

        options[value]()

        menuconsole()


def clientconsole():
    while True:
        value = int(input("""
            1 - All clients
            2 - Add a new Client
            3 - Delete a Client
            4 - Update a Client
            0 - Back
            
        """))

        options = {
            1: showclients,
            2: addclient,
            3: deleteclient,
            4: updateclients,
            0: console
        }

        options[value]()
        clientconsole()


def orderconsole():
    while True:
        value = int(input(""" 
            1 - All Orders
            2 - Add a new order
            0 - Back
            
        """))

        options = {
            1: showorders,
            2: selectclientconsole,
            0: console
        }

        options[value]()


def selectclientconsole():
    value = int(input("""  
        1 - Search client by name
        2 - Search cLient by address
        3 - Add a new client and order
        0 - Back
        
    """))

    options = {
        1: searchclientname,
        2: searchbyaddress,
        3: addclientsorder,
        0: orderconsole
    }

    options[value]()

    neworder()
