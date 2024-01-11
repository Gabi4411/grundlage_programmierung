import pickle
from abc import abstractmethod


class Datarepo:
    def __init__(self, filename):
        self.filename = filename

    def save(self, obj):
        with open(self.filename, 'wb') as file:
            pickle.dump(obj, file)

    def load(self):
        with open(self.filename, 'rb') as file:
            try:
                return pickle.load(file)
            except EOFError:
                print("Nothing in the file yet!")

    def sort(self, obj):
        obj = sorted(obj)
        self.save(obj)

    def add(self, obj):
        objectlist: list = self.load()
        objectlist.append(obj)
        self.sort(objectlist)
        print("The new item has been added successfully")

    def remove(self, idp):
        objectlist = self.load()
        if idp < len(objectlist):
            objectlist.pop(idp)
            self.save(objectlist)
            print("The item has been successfully deleted!")
            return

        print("The item hasn't been found!")

    def update(self, idp, newobj):
        objectlist: list = self.load()
        if idp < len(objectlist):
            self.remove(idp)
            self.add(newobj)
            print("The item has been successfully updated!")
            return

        print("The item hasn't been found!")

    @abstractmethod
    def convert_to_string(self, lista):
        pass

    @abstractmethod
    def convert_from_string(self, string):
        pass
