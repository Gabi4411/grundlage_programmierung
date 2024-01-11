from .id import ID


class Client(ID):
    def __init__(self, idp, name, address):
        super().__init__(idp)
        self.name = name
        self.address = address

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f"Id: {self.idp}, Name: {self.name}, Addresss: {self.address}"
