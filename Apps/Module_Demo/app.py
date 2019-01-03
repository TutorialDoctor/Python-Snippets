#from Controllers import *
#from Models import *

#from Models import flower
#from Models import animal

#f = Flower.Flower('daisy')
#print(f.name)

#a = Animal.Animal('dog')
#print(a.name)

from Models.Flower import Flower
from Models.Animal import Animal

f = Flower('rose')
print(f.name)

a = Animal('lamb')
print(a.name)

