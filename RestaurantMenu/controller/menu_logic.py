from repository.drinkrepo import DrinkRepo
from repository.cookeddishrepo import CookedDishRepo
from modelle.cookeddish import CookedDish
from modelle.drink import Drink
from .datarepo_logic import showdata


cookeddishmanager = CookedDishRepo('cookeddish.dat')
drinkmanager = DrinkRepo('drink.dat')


def showmenu():
    print("CookedDishes: ", '\n')
    showdata(0)

    print("Drinks: ", '\n')
    showdata(1)


def addcookeddish():
    name = input("Name: ")
    portionsize = int(input("Portion: "))
    price = int(input("Price: "))
    preptime = int(input("Time for the preparation:"))

    cookeddishes = cookeddishmanager.load() if cookeddishmanager.load() else []
    cookeddish = CookedDish(name, portionsize, price, preptime)
    cookeddishes.append(cookeddish)
    cookeddishmanager.sort(cookeddishes)


def adddrink():
    name = input("Name: ")
    portionsize = int(input("Portion: "))
    price = int(input("Price: "))
    alcoolvolume = int(input("Alcohol volume: "))

    drinks = drinkmanager.load() if drinkmanager.load() else []
    drink = Drink(name, portionsize, price, alcoolvolume)
    drinks.append(drink)
    drinkmanager.sort(drinks)


def search():
    name = input("What item are you searching for: ")
    cookeddishes = cookeddishmanager.load() if cookeddishmanager else []
    drinks = drinkmanager.load() if drinkmanager else []
    print('\n')
    if cookeddishes:
        print("Cooked Dishes: ", '\n')
        for idx in range(len(cookeddishes)):
            if name.lower() in cookeddishes[idx].id.lower():
                print(idx, str(cookeddishes[idx]))

    if drinks:
        print("Drinks: ", '\n')
        for idx in range(len(drinks)):
            if name.lower() in drinks[idx].id.lower():
                print(idx, str(drinks[idx]))

        return

    print("The item you are looking for doesn't exist!")


def updateitem():
    choose = int(input("""
    What do you want to update:
        1 - Cooked Dish
        2 - Drink
        
    """))
    idp = int(input("Enter the id you wnat to update: "))
    if choose == 1:
        name = input("New name: ")
        portionsize = input("New portion size: ")
        price = input("New price: ")
        preptime = input("New preparation time: ")
        cookeddish = CookedDish(name, portionsize, price, preptime)
        cookeddishmanager.update(idp, cookeddish)

    else:
        name = input("New name: ")
        portionsize = input("New portion size: ")
        price = input("New price: ")
        alcoholvolume = input("New alcohool volume: ")
        drink = Drink(name, portionsize, price, alcoholvolume)
        drinkmanager.update(idp, drink)


def showupdatedmenu():
    showmenu()
    updateitem()


def deleteitem():
    choose = int(input("""
    What item do you want to delete:
        1 - Cooked Dish
        2 - Drink
        
    """))

    idp = int(input("Enter the id you want to delete: "))

    if choose == 1:
        cookeddishmanager.remove(idp)
    else:
        drinkmanager.remove(idp)


def showmenuafterdelete():
    showmenu()
    deleteitem()
