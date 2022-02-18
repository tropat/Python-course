from points import Point
import math

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):        # "Circle(x, y, radius)"
        return "Circle("+str(self.pt.x)+", "+str(self.pt.y)+", "+str(self.radius)+")"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return math.pi*pow(self.radius,2)

    def move(self, x, y):     # przesuniecie o (x, y)
        return Circle(self.pt.x+x, self.pt.y+y, self.radius)

    def cover(self, other):    # najmniejszy okrąg pokrywający oba
        if math.sqrt(pow(self.pt.x-other.pt.x,2)+pow(self.pt.y-other.pt.y, 2)) <= abs(self.radius-other.radius):
            if self.radius >= other.radius:
                return Circle(self.pt.x, self.pt.y, self.radius)
            else:
                return Circle(other.pt.x, other.pt.y, other.radius)
        else:
            return Circle(min(self.pt.x, other.pt.x)+abs(self.pt.x-other.pt.x)/2,min(self.pt.y, other.pt.y)+abs(self.pt.y-other.pt.y)/2,(math.sqrt(pow(self.pt.x-other.pt.x,2)+pow(self.pt.y-other.pt.y, 2))+self.radius+other.radius)/2)

# Kod testujący moduł.

import unittest

class TestCircle(unittest.TestCase): 
    def setUp(self):
        try:
            self.c1 = Circle(1,1,1)
            self.c3 = Circle(3,4, 2)
            self.c4 = Circle(1,1, 1)
        except ValueError:
            print("setUp: Bad Values")

    def test__init__(self):
        try:
            self.c2 = Circle(2,5, -1)
        except ValueError:
            print("c2: Bad values")

    def test__repr__(self):
        self.assertEqual(repr(self.c1), "Circle(1, 1, 1)")
        self.assertEqual(repr(self.c3),"Circle(3, 4, 2)")

    def test__eq__(self):
        self.assertEqual(self.c1 == self.c4, True)
        self.assertEqual(self.c3 == self.c1, False)

    def test__ne__(self):
        self.assertEqual(self.c1 != self.c4, False)
        self.assertEqual(self.c3 != self.c1, True)

    def test_area(self):
        self.assertEqual(self.c1.area(), math.pi)
        self.assertEqual(self.c3.area(), math.pi*4)

    def test_move(self):
        self.assertEqual(self.c1.move(2,3), Circle(3,4,1))
        self.assertEqual(self.c3.move(-2,1), Circle(1,5,2))

    def test_cover(self):
        self.assertEqual(self.c1.cover(self.c3), Circle(2, 2.5, (math.sqrt(13)+3)/2))
        self.assertEqual(self.c1.cover(self.c4), Circle(1,1,1))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()

