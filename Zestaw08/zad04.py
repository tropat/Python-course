import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if a+b<=c or a+c<=b or b+c<=a or a<=0 or b<=0 or c<=0:
        raise ValueError
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

import unittest

class TestHeron(unittest.TestCase): 
    def setUp(self): pass

    def test(self):
        self.assertRaises(ValueError, heron, 1, 2, 3)
        self.assertEqual(heron(3,4,5), 6.0)
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()

