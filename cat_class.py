class Cat:
    species = 'mammal'

    # initialize/ instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    # instance method
    def description(self):
        return '{} is {}'.format(gus.name, gus.age)

gus = Cat('Gus', 9)
print(gus.description())