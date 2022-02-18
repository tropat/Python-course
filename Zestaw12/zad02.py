def binarne_rek(L,left,right,y):
    if left <= right:
        mid = (left + right) // 2
        if L[mid] == y:
            return mid
        elif L[mid] > y:
            return binarne_rek(L,left,mid-1,y)
        else:
            return binarne_rek(L,mid+1,right,y)
    else:
        return -1

import random

n = 100
k = 10

sortedList = list()

for i in range(0,n*2,2):
    sortedList.append(i)

y = random.randint(0,n-1)

print(sortedList)
print(y)
print(binarne_rek(sortedList,0,len(sortedList)-1,y))