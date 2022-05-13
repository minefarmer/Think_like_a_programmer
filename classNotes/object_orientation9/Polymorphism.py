'''         Polymorphism
Polymorphism means that differient objects can behave in differient ways for the same message (FunctionCall)
Consequently, sender of a message does not need to know exact class of reciever

Example - Drawing Application

                    Drawing Pane    Sender Object
                        /|\
                       / | \
                      /  |  \
                     /   |   \
                    /    |    \
                   /     |     \
                  /      |      \
          draw   /     draw     draw
                /        |        \
         Triangle      circle    Rectangle
            |____________|___________|
                  Reciever Objects


            Polymorphism (Wikipedia)
In programming langues, polymorphism is the provision of a single interface to entities of differient types.
A polymorphic type is one whose operations can also be applied to values of some other type, or types.

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
    def getName(self):
        return self.__name

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


animals = [Lion("Woofie")], Cat("Max")

for animal in animals:
    print(animal.getName())
    print(animal.makeNoise())
    print(animal.eat())
    
        # Traceback (most recent call last):
        # File "/home/carl/Desktop/MatsHub/Think_like_a_programmer/classNotes/object_orientation9/Polymorphism.py", line 73, in <module>
        #     print(animal.getName())
        # AttributeError: 'list' object has no attribute 'getName'
