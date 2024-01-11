from .datarepo import Datarepo


class OrderRepo(Datarepo):
    def __init__(self, filename):
        super().__init__(filename)

    def convert_to_string(self, lista):
        return map(lambda x: str(x), lista)

    def convert_from_string(self, string):
        objectlist = []
        return map(lambda x: objectlist.append(x), string)
