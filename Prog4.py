class Person:

    def __init__(self, name: str, lname: str):
        self.name = name
        self.lname = lname

    def first(self):
        return self.name
    
    @property
    def last(self):
        return self.lname
    

per1 = Person('Jo', 'Tyler')

print(per1.first())

print(per1.last)

