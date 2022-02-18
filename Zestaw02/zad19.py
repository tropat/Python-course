L = [123, 32, 2, 126, 43, 843, 3, 52, 237, 93, 231]

liczby = [str(liczba).zfill(3) for liczba in L]

napis = ''
for wyraz in liczby:
    napis += wyraz
    napis += ' '

print(napis)