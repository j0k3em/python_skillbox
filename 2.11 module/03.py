import math


class Circle:
    def __init__(self, x, y, r):
        self.X = x
        self.Y = y
        self.radius = r

    def get_square(self):
        return math.pi * self.radius ** 2

    def get_perimetr(self):
        return 2 * math.pi * self.radius

    def make_bigger(self, count):
        self.radius *= count

    def isInterceted(self, another_circle):
        return (self.X - another_circle.X) ** 2 +\
               (self.Y - another_circle.Y) ** 2 <= (self.radius + another_circle.radius) ** 2
