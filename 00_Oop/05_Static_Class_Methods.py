# Static and class methods in python. This video explains 
# the difference between static and class methods and how to 
# properly implement them in python. I also mention class variables as well.

class Dog:
    dogs =[]

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    # class method doesn't require creation of a class instance
    @classmethod
    # the class is bound to the method as the first argument (cls) ->
    # this is means that it is easy to access class, in the method,
    # via cls arugment, instead of having to use the full class name
    def num_dogs(cls):
        return len(cls.dogs)

    # static method knows nothing about the class and just deals
    # with parameters
    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print('Bark!')

tim = Dog("Tim")
jim = Dog("Jim")

print(Dog.bark(6))
print(Dog.num_dogs())


