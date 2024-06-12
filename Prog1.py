from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def pet(self):
        print("Animal is a pet")


class Dog(Animal):

    def pet(self):
        print("This animal is a puppy")


class Cat(Animal):

    def pet(self):
        print("This animal is a kitten")


class Lizard(Animal):

    def pet(self):
        print("This animal is a lizard")


dog = Dog()
cat = Cat()
lizard = Lizard()

dog.pet()
cat.pet()
lizard.pet()

