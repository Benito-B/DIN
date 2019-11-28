class Point(object):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class LineSegment(object):

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def slope(self) -> float:
        return abs(self.p2.y - self.p1.y) / abs(self.p2.x - self.p1.x)

    def length(self) -> float:
        return ((self.p2.x - self.p1.x)**2 + (self.p2.y - self.p1.y)**2)**0.5


if __name__ == "__main__":
    segment = LineSegment(Point(1, 1), Point(3, 2))
    print(segment.slope())
    print(segment.length())
