from .id import ID


class Dish(ID):
    def __init__(self, idp, portionsize, price):
        super().__init__(idp)
        self.portionsize = portionsize
        self.price = price
