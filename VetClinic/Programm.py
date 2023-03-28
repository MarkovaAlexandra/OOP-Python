from Cat import Cat
from Dog import Dog
from Vetservice import Vetservice

cat1 = Cat("Murka",4,5,True)
dog1 = Dog("Bobik",10,25,False)
vetclinic = Vetservice()
vetclinic.add_animal(cat1)
vetclinic.add_animal(dog1)
vetclinic.print_clinic()
vetclinic.del_animal(cat1)
vetclinic.print_clinic()