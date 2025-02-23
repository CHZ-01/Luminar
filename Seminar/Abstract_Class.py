# importing modules to use abstraction
from abc import ABC, abstractmethod

# creating an abstract class, cannot be called directly
class Animal(ABC):
    # defining an abstract method in the abstract class
    @abstractmethod
    def move(self):
        pass

# creating child classes inheriting from the abstract class
class Dog(Animal):
    # overriding the abstract method in the child class
    def move(self):
        print("Dog: I protect my home.")

# creating child classes inheriting from the abstract class
class Cat(Animal):
    # overriding the abstract method in the child class
    def move(self):
        print("Cat: I do nothing.")

# creating objects of Dog & Cat class and calling the move method
obj_dog = Dog()
obj_dog.move()
obj_cat = Cat()
obj_cat.move()