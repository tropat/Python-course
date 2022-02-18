def odwracanieIteracja(L, left, right):
    while left < right:
        pom = L[left]
        L[left] = L[right]
        L[right] = pom 
        left += 1
        right -= 1

def odwracanieRekurencja(L, left, right):
    if left < right:
        pom = L[left]
        L[left] = L[right]
        L[right] = pom
        odwracanieRekurencja(L, left+1, right-1)

L = [2,4,2,6,4,37,83,1]
print(L)
odwracanieIteracja(L, 2, 6)
print(L)
odwracanieRekurencja(L, 1, 6)
print(L)