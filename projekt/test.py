import unittest
from bst import *

class TestBST(unittest.TestCase): 
    def setUp(self): 
        self.b = BinarySearchTree()

    def test_search(self):
        self.b.insert(1) 
        self.assertEqual(self.b.search(1).data,1)
        self.assertEqual(self.b.search(2),None)
        
    def test_insert(self): 
        self.b.insert(1)
        self.assertEqual(self.b.root.data,1)
        self.b.insert(2)
        self.assertEqual(self.b.search(2).parent.data,1)
        self.b.insert(-3)
        self.assertEqual(self.b.search(-3).parent.data,1)
        self.b.insert(10)
        self.assertEqual(self.b.search(10).parent.data,2)
        self.b.insert(-1)
        self.assertEqual(self.b.search(-1).parent.data,-3)
        self.b.insert(-7)
        self.assertEqual(self.b.search(-7).parent.data,-3)
        self.b.insert(7)
        self.assertEqual(self.b.search(7).parent.data,10)
        self.b.insert(11)
        self.assertEqual(self.b.search(11).parent.data,10)
        self.b.insert(9)
        self.assertEqual(self.b.search(9).parent.data,7)
        self.b.insert(-10)
        self.assertEqual(self.b.search(-10).parent.data,-7)
        self.b.insert(-11)
        self.assertEqual(self.b.search(-11).parent.data,-10)
        self.b.insert(-12)
        self.assertEqual(self.b.search(-12).parent.data,-11)
    
    def test_is_empty(self):
        self.assertTrue(self.b.is_empty())
        self.b.insert(3)
        self.assertFalse(self.b.is_empty())

    def test_delete(self): 
        self.b.insert(1)
        self.b.delete(1)
        self.assertTrue(self.b.is_empty())
        self.b.insert(2)
        self.b.insert(-3)
        self.b.insert(10)
        self.b.insert(-1)
        self.b.insert(0)
        self.b.delete(-3)
        self.assertEqual(self.b.search(-3),None)

    def test_dsw(self): 
        self.b.insert(1)
        self.b.insert(-3)
        self.b.insert(10)
        self.b.insert(-1)
        self.b.insert(-7)
        self.b.insert(7)
        self.b.insert(11)
        self.b.insert(9)
        self.b.insert(-10)
        self.b.insert(-11)
        self.b.insert(-12)
        self.b.dsw()
        self.assertEqual(self.b.search(-12).parent.data,-11)
        self.assertEqual(self.b.search(-11).parent.data,-7)
        self.assertEqual(self.b.search(-10).parent.data,-11)
        self.assertEqual(self.b.search(-7).parent.data,7)
        self.assertEqual(self.b.search(-3).parent.data,-1)
        self.assertEqual(self.b.search(-1).parent.data,-7)
        self.assertEqual(self.b.search(1).parent.data,-1)
        self.assertEqual(self.b.search(7).parent,None)
        self.assertEqual(self.b.search(9).parent.data,10)
        self.assertEqual(self.b.search(10).parent.data,7)
        self.assertEqual(self.b.search(11).parent.data,10)

    def test_reset(self): 
        self.b.insert(1)
        self.b.reset()
        self.assertTrue(self.b.is_empty())

if __name__ == '__main__':
    unittest.main()

