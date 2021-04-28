# Private vs Public classes in python. In python there is actually 
# no such thing as private or public class. So to simulate this 
# we use conventions to describe which methods and classes we would like 
# to tell other programmers should be private. 

class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("Hello")

    def display(self):
        print('Hi')

jim = NotPrivate('JIM')
