from Cat import Cat
from Dog import Dog

class Vetservice():
    def __init__(self):
        list = []
        self._list = list

    def add_animal(self, animal):
        self._list.append(animal)

    def del_animal(self, animal):
        self._list.remove(animal)

    def print_clinic(self):
        for el in self._list:
            print(str(el))