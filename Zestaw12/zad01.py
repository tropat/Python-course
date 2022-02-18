import random

n = 100
k = 10

L = list()

for i in range(0,n):
    L.append(random.randint(0,k-1))

y = random.randint(0,k-1)

def find_positions(x):
    l = list()
    for i in range(0,n):
        if L[i] == x:
            l.append(i)
    return l

def find_how_many(x):
    sum = 0
    for i in range(0,n):
        if L[i] == x:
            sum += 1
    return sum

print(L)
print(y)
print(find_positions(y))
print(find_how_many(y))