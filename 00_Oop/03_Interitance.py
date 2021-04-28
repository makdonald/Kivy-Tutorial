class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print('Every animal has own sound')

class Cat(Animal):
    def __init__(self, name, age, color):
        # call the initialization of Animal
        super().__init__(name, age)
        self.color = color

    # overwrite talk method from Animal class
    def talk(self):
        print('Meow!')

tim = Cat('tim', 5, 'green')
tim.speak()
tim.talk()

class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed
    
    def horn_sound(self):
        print('beep beep')

class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def horn_sound(self):
        print('Bu Bu')

bmw = Car(25000, 90, 'blue', 280)
jelcz = Truck(12500, 70, 'black', 6)

print(bmw.horn_sound())
print(jelcz.horn_sound())