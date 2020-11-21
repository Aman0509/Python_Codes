import math


class Circle:

    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2*math.pi*self.radius


obj1 = Circle(5)
print(obj1.area())
print(obj1.circumference())
