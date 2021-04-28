class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old')

    def change_age(self,age):
        self.age = age

    def add_weigth(self, weigth):
        self.weight = weigth

tim = Dog('Tim', 11)
fred = Dog('Fred', 5)

print(tim.name)
print(fred.speak())

fred.change_age(7)
print(fred.age)

tim.add_weigth(22)
print(tim.weight)