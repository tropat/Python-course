from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return "["+str(self.pt1)+", "+str(self.pt2)+"]"

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle("+str(self.pt1.x)+", "+str(self.pt1.y)+", "+str(self.pt2.x)+", "+str(self.pt2.y)+")"

    def __eq__(self, other):    # obsługa rect1 == rect2
        return self.pt1==other.pt1 and self.pt2==other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point((self.pt1.x+self.pt2.x)/2,(self.pt1.y+self.pt2.y)/2)

    def area(self):             # pole powierzchni
        return (self.pt2.x-self.pt1.x)*(self.pt2.y-self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        return Rectangle(self.pt1.x+x,self.pt1.y+y,self.pt2.x+x,self.pt2.y+y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): 

    def setUp(self):
        self.rec1 = Rectangle(1,2,3,4)
        self.rec2 = Rectangle(-1,-3,5,7)
        self.rec3 = Rectangle(1,2,3,4)

    def test__str__(self):
        self.assertEqual(str(self.rec1), "[(1, 2), (3, 4)]")
        self.assertEqual(str(self.rec2), "[(-1, -3), (5, 7)]")

    def test__repr__(self): 
        self.assertEqual(repr(self.rec1), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(repr(self.rec2), "Rectangle(-1, -3, 5, 7)")

    def test__eq__(self): 
        self.assertEqual(self.rec2==self.rec1, False)
        self.assertEqual(self.rec1==self.rec3, True)

    def test__ne__(self): 
        self.assertEqual(self.rec2!=self.rec1, True)
        self.assertEqual(self.rec1!=self.rec3, False)

    def test_center(self): 
        self.assertEqual(self.rec1.center(), Point(2,3))
        self.assertEqual(self.rec2.center(), Point(2,2))

    def test_area(self): 
        self.assertEqual(self.rec1.area(), 4)
        self.assertEqual(self.rec2.area(), 60)

    def test_move(self): 
        self.assertEqual(self.rec1.move(1,2), Rectangle(2,4,4,6))
        self.assertEqual(self.rec2.move(-1,-2), Rectangle(-2,-5,4,5))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()