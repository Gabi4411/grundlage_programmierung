from .id import ID
from functools import reduce
from controller.menu_logic import drinkmanager, cookeddishmanager


class Order(ID):
    total = 0

    def __init__(self, idp, clientid, dishids, drinkids):
        super().__init__(idp)
        self.clientid = clientid
        self.dishids = dishids
        self.drinkids = drinkids

    def calculatecost(self):
        cookeddishlist = cookeddishmanager.load()
        drinklist = drinkmanager.load()
        prices = []

        for dish in cookeddishlist:
            if dish.idp in self.dishids:
                prices.append(int(dish.price))

        for drink in drinklist:
            if drink.idp in self.drinkids:
                prices.append(int(drink.price))

        self.total = reduce(lambda x, y: x + y, prices)

    def __generatereceipt(self):
        self.calculatecost()
        cookeddishlist = cookeddishmanager.load()
        drinklist = drinkmanager.load()
        receipt = f"Order: {self.idp} for the client with the id {self.clientid}" + '\n'

        ids = []
        prices = []

        for dish in cookeddishlist:
            if dish.idp in self.dishids:
                ids.append(dish.idp)
                prices.append(str(dish.price))

        for drink in drinklist:
            if drink.idp in self.drinkids:
                ids.append(drink.idp)
                prices.append(str(drink.price))

        items = list(map(lambda x, y: f"Item: {x},  Price: {y}" + '\n', ids, prices))

        receipt += "".join(items)
        receipt += f"Order total: {str(self.total)}" + '\n'
        receipt += "Thank you for your order!"

        return receipt

    def printreceipt(self):
        receipt = self.__generatereceipt()
        print(receipt)

    def __lt__(self, other):
        return self.idp < other.idp

    def __str__(self):
        return f"Order: {self.idp}, Client: {self.clientid}, Dishes: {self.dishids}, Drinks: {self.drinkids}"
