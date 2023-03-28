from Animal import Animal

class Dog(Animal):
    def __init__(self, nickname,age,weight,ishungry):
        super().__init__(nickname)
        self._age = age
        self._weight = weight
        self._ishungry = ishungry

    @property
    def age(self):
        return self._age
    
    @property
    def weight(self):
        return self._weight

    @property
    def ishungry(self):
        return self._ishungry

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    @ishungry.setter
    def ishungry(self, new_ishungry):
        self._ishungry = new_ishungry

    def __str__(self) -> str:
        return f"{self.nickname} {self._age} {self._weight} {self._ishungry}"