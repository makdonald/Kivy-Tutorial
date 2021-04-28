# Classes and objects
# overloading methods such as __gt__, __len__, __eq__ and 
# other python builtins to allow for operations and comparisons 
# on your created objects.

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))
    # p - is another point object
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point(self.x * p.x, self.y * p.y) 
   

    def __gt__(self, p):
        return self.length() > p.length()



    def __str__(self):
        return ('(' + str(self.x) +','+ str(self.y) + ')' )


p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

sumofp = p1 + p3
sub = p3 - p4
mult = p2 * p3
print(mult)

print(p1 < p4)

print(p1.length())
print(len(p1))

