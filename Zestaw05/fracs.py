import math

def nww(a,b):
    return a*b//math.gcd(a,b)

def nwd(frac):
    if(frac[1] < 0):
        frac[1] = -frac[1]
        frac[0] = -frac[0]
    if frac[0] == 0:
        return [0,1]
    gcd = math.gcd(frac[0], frac[1])
    return [frac[0]//gcd, frac[1]//gcd]

def add_frac(frac1, frac2):         # frac1 + frac2  
    frac = [(int)(frac1[0]*frac2[1] + frac1[1]*frac2[0]), (int)(frac1[1]*frac2[1])]
    return nwd(frac)

def sub_frac(frac1, frac2):         # frac1 - frac2
    frac = [(int)(frac1[0]*frac2[1] - frac1[1]*frac2[0]), (int)(frac1[1]*frac2[1])]
    return nwd(frac)

def mul_frac(frac1, frac2):         # frac1 * frac2
    frac = [(int)(frac1[0]*frac2[0]), (int)(frac1[1]*frac2[1])]
    return nwd(frac)

def is_zero(frac):                  # bool, typu [0, x]
    if frac[0] == 0:
        return True
    else: return False

def div_frac(frac1, frac2):         # frac1 / frac2
    if not is_zero(frac2):
        frac = [(int)(frac1[0]*frac2[1]), (int)(frac1[1]*frac2[0])]
        return nwd(frac)
    return -1

def is_positive(frac):              # bool, czy dodatni
    if frac[0]*frac[1] > 0:
        return True
    else: return False

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    n = nww(frac1[1], frac2[1])
    frac12 = [(int)(frac1[0]*(n/frac1[1])), (int)(n)]
    frac22 = [(int)(frac2[0]*(n/frac2[1])), (int)(n)]
    if frac12[0] == frac22[0]:
        return 0
    elif frac12[0] > frac22[0]:
        return 1
    else:
        return -1

def frac2float(frac):               # konwersja do float
    return (float)(frac[0]/frac[1])

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [1, 2]), [1, 1])
        self.assertEqual(add_frac([6, 4], [1, 6]), [5, 3])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([-1, 2], [1, 3]), [-5, 6])
        self.assertEqual(sub_frac([6, 4], [1, 6]), [4, 3])
        self.assertEqual(sub_frac([-1, 2], [-1, 2]), [0, 1])

    def test_mul_frac(self): 
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([4, 2], [1, 2]), [1, 1])
        self.assertEqual(mul_frac([0, 2], [1, 3]), [0, 1])
        self.assertEqual(mul_frac([1, -2], [1, 3]), [-1, 6])

    def test_div_frac(self): 
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([1, 2], [0, 1]), -1)
        self.assertEqual(div_frac([5, 2], [1, 2]), [5, 1])
        self.assertEqual(div_frac([10, 12], [-1, 3]), [-5, 2])

    def test_is_positive(self): 
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([0, 2]), False)

    def test_is_zero(self): 
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([-1, 1]), False)
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([0, -1]), True)

    def test_cmp_frac(self): 
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([-1, 2], [2, -4]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, 3]), -1)
        self.assertEqual(cmp_frac([6, 2], [1, 2]), 1)
        self.assertEqual(cmp_frac([0, 1], [0, 4]), 0)

    def test_frac2float(self): 
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, -4]), -0.25)
        self.assertEqual(frac2float([0, 2]), 0.0)
        self.assertEqual(frac2float([5, 5]), 1.0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy