liczba = 1020459438543260100342583024300

napis = str(liczba)
ile = 0

for char in napis:
    if char == '0':
        ile += 1

print(ile)