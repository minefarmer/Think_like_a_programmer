'''         Abstract Classes line 11








'''
from abc import ABC, abstractmethod
from unicodedata import name

class Animal (ABC):
    
    def __init__(self):
        self.__name = name
    
    @abstractmethod
    def makeNoise(self):pass
    
    @abstractmethod
    def eat(self):pass
        
    def move(self):
        print("I can move anywhere")

class Lion(Animal):
    
    def __init__(self, name):
        super().__init__()
    
    def makeNoise(self):
        print("Meow meow...")

    def eat(self):
        print("I can eat buffaloes, zebras, young elephants")

class Cat(Animal):
    
    def __init__(self, name):
        super().__init__()
    
    def makeNoise(self):
        print("I can roar...")

    def eat(self):
        print("I can eat mouses...")


lion = Lion("Lion")
lion.makeNoise()
lion.eat()

cat = Cat("Cat")
cat.makeNoise()
cat.eat()

                # Meow meow...
                # I can eat buffaloes, zebras, young elephants
                # I can roar...
                # I can eat mouses..
