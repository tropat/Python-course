from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            raise ValueError
        else:
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

    def intersection(self, other):
        if min(self.pt2.x,other.pt2.x) > max(self.pt1.x,other.pt1.x) and min(self.pt2.y,other.pt2.y) > max(self.pt1.y,other.pt1.y):
            return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y)) 
        else:
            raise ValueError

    def cover(self, other):
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y)) 

    def make4(self):
        r1 = Rectangle(self.pt1.x, self.pt1.y, self.pt1.x+(self.pt2.x-self.pt1.x)/2, self.pt1.y+(self.pt2.y-self.pt1.y)/2)
        r2 = Rectangle(self.pt1.x, self.pt1.y+(self.pt2.y-self.pt1.y)/2,  self.pt1.x+(self.pt2.x-self.pt1.x)/2, self.pt2.y)
        r3 = Rectangle(self.pt1.x+(self.pt2.x-self.pt1.x)/2, self.pt1.y, self.pt2.x, self.pt1.y+(self.pt2.y-self.pt1.y)/2)
        r4 = Rectangle(self.pt1.x+(self.pt2.x-self.pt1.x)/2, self.pt1.y+(self.pt2.y-self.pt1.y)/2, self.pt2.x, self.pt2.y)
        return (r1,r2,r3,r4)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): 

    def setUp(self):
        try:
            self.rec1 = Rectangle(1,2,3,4)
            self.rec2 = Rectangle(-1,-3,5,7)
            self.rec3 = Rectangle(1,2,3,4)
            self.rec5 = Rectangle(2,3,8,5)
            self.rec6 = Rectangle(0,0,1,1)
        except ValueError:
            print("setUp: Bad values")

    def test__init__(self):
        try:
            self.rec4 = Rectangle(3,1,2,8)
        except ValueError:
            print("rec4: Bad values")

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

    def test_intersection(self):
        try:
            intersection = self.rec1.intersection(self.rec5)
            self.assertEqual(intersection, Rectangle(2,3,3,4))
        except ValueError:
            print("rec1 i rec5 rozlaczne")
        try:
            intersection = self.rec2.intersection(self.rec2)
            self.assertEqual(intersection, Rectangle(-1,-3,5,7))
        except ValueError:
            print("rec2 i rec2 rozlaczne")
        try:
            intersection = self.rec1.intersection(self.rec6)
        except ValueError:
            print("rec1 i rec6 rozlaczne")

    def test_cover(self):
        self.assertEqual(self.rec1.cover(self.rec1), Rectangle(1,2,3,4))
        self.assertEqual(self.rec1.cover(self.rec6), Rectangle(0,0,3,4))

    def test_make4(self):
        t1 = (Rectangle(1,2,2,3), Rectangle(1,3,2,4), Rectangle(2,2,3,3), Rectangle(2,3,3,4))
        t2 = self.rec1.make4()
        self.assertEqual(t1[0], t2[0])
        self.assertEqual(t1[1], t2[1])
        self.assertEqual(t1[2], t2[2])
        self.assertEqual(t1[3], t2[3])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()