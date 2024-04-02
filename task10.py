from numpy import sqrt, sign


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


class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = (sign(point1.x) != sign(point2.x)) != (sign(point1.y) != sign(point2.y))


class CoordinateSystem:
    segments = []

    def add_segment(self, segment):
        self.segments.append(segment)

    def axis_intersection(self):
        return sum([1 for segm in self.segments if segm.one_intersection])


a = Segment(Point((1, 1)), Point((-1, -1)))
print(a.one_intersection)
b = Segment(Point((1, 1)), Point((1, -1)))
print(b.one_intersection)
c = Segment(Point((1, 1)), Point((1, 1)))
print(c.one_intersection)

system = CoordinateSystem()
system.add_segment(a)
system.add_segment(b)
system.add_segment(c)

print(system.axis_intersection())
