line = "jakis dlugi lancuch znakowy zeby bylo duzo wyrazow la la lalalalala"

wyrazy = line.split()

maksymalny = wyrazy[0]
for wyraz in wyrazy:
    if len(wyraz) > len(maksymalny):
        maksymalny = wyraz

print(maksymalny, ' ', str(len(maksymalny)))