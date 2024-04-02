from numpy import sqrt


class Point:
    def __init__(self, coord=(0, 0)):
        self.x = coord[0]
        self.y = coord[1]

    def __repr__(self):
        return f'x={self.x}; y={self.y}'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance(self, other):
        return sqrt((self.get_x() - other.get_x())**2 + (self.get_y() - other.get_y())**2)

    def sum(self, other):
        return Point((self.get_x() + other.get_x(), self.get_y() + other.get_y()))


a = Point((2, 3))
b = Point((6, 6))
print({'a_point': a, 'b_point': b})
print(a.distance(b))
c = a.sum(b)
print(c)
