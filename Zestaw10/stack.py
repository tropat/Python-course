class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise MemoryError
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise MemoryError
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

import unittest

class TestStack(unittest.TestCase): 
    def setUp(self):
        self.s1 = Stack()
        self.s2 = Stack(4)
        self.s3 = Stack(1)

        self.s1.push(1)
        self.s1.push(2)
        self.s1.push(3)

        self.s3.push(5)

    def test_is_full(self):
        self.assertFalse(self.s2.is_full())
        self.assertTrue(self.s3.is_full())

    def test_is_empty(self):
        self.assertFalse(self.s1.is_empty())
        self.assertTrue(self.s2.is_empty())
    
    def test_push(self):
        self.assertRaises(MemoryError, lambda: self.s3.push(5))

    def test_pop(self):
        self.assertEqual(self.s1.pop(), 3)
        self.assertEqual(self.s1.pop(), 2)
        self.assertRaises(MemoryError, lambda: self.s2.pop())

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()