#Bledne sredniki na koncach
#Poprawione:
x = 2; y = 3

if(x > y):
    result = x
else:
    result = y

print("----------------------")

#Brak wciec
#Poprawione:
for i in "qwerty":
    if ord(i) < 100: print(i)

print("----------------------")

#Kod w porzadku
for i in "axby": print(ord(i) if ord(i) < 100 else i)