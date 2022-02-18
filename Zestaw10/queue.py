class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.n == self.head

    def put(self, data):
        if self.is_full():
            raise MemoryError
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise MemoryError
        data = self.items[self.head]
        self.items[self.head] = None   # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data

import unittest

class TestStack(unittest.TestCase): 
    def setUp(self):
        self.q1 = Queue()
        self.q2 = Queue(4)
        self.q3 = Queue(1)

        self.q1.put(1)
        self.q1.put(2)
        self.q1.put(3)

        self.q3.put(4)

    def test_is_full(self):
        self.assertFalse(self.q2.is_full())
        self.assertTrue(self.q3.is_full())

    def test_is_empty(self):
        self.assertFalse(self.q1.is_empty())
        self.assertTrue(self.q2.is_empty())

    def test_put(self):
        self.assertRaises(MemoryError, lambda: self.q3.put(5))

    def test_get(self):
        self.assertEqual(self.q1.get(), 1)
        self.assertEqual(self.q1.get(), 2)
        self.assertRaises(MemoryError, lambda: self.q2.get())

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()