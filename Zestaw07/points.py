from numpy import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return "("+str(self.x)+", "+str(self.y)+")"

    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point("+str(self.x)+", "+str(self.y)+")"

    def __eq__(self, other):    # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return sqrt(pow(self.x,2)+pow(self.y,2))

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 

    def setUp(self):
        self.point1 = Point(1,2)
        self.point2 = Point(5,-3)
        self.point3 = Point(1,2)

    def test__str__(self): 
        self.assertEqual(str(self.point1), "(1, 2)")
        self.assertEqual(str(self.point2), "(5, -3)")

    def test__repr__(self):
        self.assertEqual(repr(self.point1), "Point(1, 2)")
        self.assertEqual(repr(self.point2), "Point(5, -3)")

    def test__eq__(self):
        self.assertEqual(self.point2==self.point1, False)
        self.assertEqual(self.point1==self.point3, True)

    def test__ne__(self):
        self.assertEqual(self.point2!=self.point1, True)
        self.assertEqual(self.point1!=self.point3, False)

    def test__add__(self):
        self.assertEqual(self.point2+self.point1, Point(6,-1))
        self.assertEqual(self.point1+self.point3, Point(2,4))

    def test__sub__(self): 
        self.assertEqual(self.point2-self.point1, Point(4,-5))
        self.assertEqual(self.point1-self.point3, Point(0,0))

    def test__mul__(self):
        self.assertEqual(self.point2*self.point1, -1)
        self.assertEqual(self.point1*self.point3, 5)

    def test_cross(self):
        self.assertEqual(self.point2.cross(self.point1), 13)
        self.assertEqual(self.point1.cross(self.point3), 0)

    def test_length(self): 
        self.assertEqual(self.point1.length(), sqrt(5))
        self.assertEqual(self.point2.length(), sqrt(34))

    def test__hash__(self):
        self.assertEqual(hash(self.point1), hash((1,2)))
        self.assertEqual(hash(self.point2), hash((5,-3)))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()