from .dish import Dish


class CookedDish(Dish):
    def __init__(self, idp, portionsize, price, preptime):
        super().__init__(idp, portionsize, price)
        self.preptime = preptime

    def __lt__(self, other):
        return self.idp < other.idp

    def __iter__(self):
        return iter(self.idp, self.price)

    def __str__(self):
        return f"Id: {self.idp}, Portionsize: {self.portionsize}, Price: {self.price}, Preptime: {self.preptime}"
