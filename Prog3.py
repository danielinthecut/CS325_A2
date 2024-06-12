from dataclasses import dataclass

class Car:

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


car = Car('Dodge', 399)
print(car.name)
print(car.price)

@dataclass
class Car:
    name: str
    price: int

car = Car('Dodge', 799)
print(car)
