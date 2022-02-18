'''P(0, 0) = 0.5,
P(i, 0) = 0.0 dla i > 0,
P(0, j) = 1.0 dla j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.'''

tab = {}

def P(a,b):
    if (a,b) not in tab.keys():
        if a >= 0 and b >= 0:
            if a==0 and b==0:
                tab[(a,b)] = 0.5
            elif a != 0 and b == 0:
                tab[(a,b)] = 0.0
            elif a == 0 and b != 0:
                tab[(a,b)] = 1.0
            else:
                tab[(a,b)] = 0.5 * (P(a-1, b) + P(a, b-1))
    return tab[(a,b)]

print(P(0,0))
print(tab)
print(P(2,1))
print(tab)
print(P(1,5))
print(tab)
print(P(2,3))
print(tab)