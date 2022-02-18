#!/usr/bin/python

import random
import numpy as np

def int_list_not_sorted(n):
    l = list()
    for i in range(0,n):
        l.append(i)
    random.shuffle(l)
    return l

def int_list_almost_sorted(n):
    l = list()
    for i in range(0,n-1,2):
        l.append(i+1)
        l.append(i)
    return l

def int_list_almost_sorted_reversed(n):
    l = list()
    for i in range(n-1,0,-2):
        l.append(i-1)
        l.append(i)
    return l

def float_list_not_sorted_gauss(n):
    l = list()
    l = np.random.normal(size=n)
    return l

def int_list_not_sorted_repetitive(n,k):
    l = list()
    for i in range(0,n):
        l.append(random.randrange(0,k))
    return l
    

import unittest

class TestHeron(unittest.TestCase): 
    def setUp(self): 
        self.n=10
        self.k=5

    def test(self):
        print(int_list_not_sorted(self.n))
        print(int_list_almost_sorted(self.n))
        print(int_list_almost_sorted_reversed(self.n))
        print(float_list_not_sorted_gauss(self.n))
        print(int_list_not_sorted_repetitive(self.n,self.k))
        
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()


