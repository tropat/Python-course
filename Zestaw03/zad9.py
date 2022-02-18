lista = [[],[4],(1,2),[3,4],(5,6,7)]
sumy = []

for i in lista:
    suma = 0
    for j in i:
        suma += j
    sumy.append(suma)

print(sumy)