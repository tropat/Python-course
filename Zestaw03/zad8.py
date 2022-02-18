sekwencja1 = "oopse231s"
sekwencja2 = "oeewr092sc"

powtorzenia = set()
wszystkich = set()

for i in sekwencja1:
    if(i not in powtorzenia and i in sekwencja2):
        powtorzenia.add(i)

for i in sekwencja1:
    if(i not in wszystkich):
        wszystkich.add(i)

for i in sekwencja2:
    if(i not in wszystkich):
        wszystkich.add(i)

print(powtorzenia)
print(wszystkich)