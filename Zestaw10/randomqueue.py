import math
import random

class RandomQueue:

    def __init__(self):
        self.items = []
        self.size = 0

    def insert(self, item): 
        self.items.append(item)
        self.size += 1

    def remove(self):    # zwraca losowy element
        if self.size == 0:
            return None
        index = math.floor(random.random()*(self.size-1))
        pom = self.items[index]
        self.items[index] = self.items[self.size-1]
        self.size -= 1
        return pom

    def is_empty(self):
        return not self.items

    def is_full(self): 
        return False

    def clear(self):     # czyszczenie listy
        self.items.clear()

rq = RandomQueue()
if rq.is_empty():
    print("pusty")
rq.insert(1)
rq.insert(2)
rq.insert(3)
rq.insert(4)

print(rq.items)

print(rq.remove())
print(rq.remove())
print(rq.remove())

if not rq.is_empty():
    print("nie pusty")

rq.clear()

if rq.is_empty():
    print("pusty")