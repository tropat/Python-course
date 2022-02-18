word = "word"

napis = ""

for char in word[:-1]:
    napis += char
    napis += '_'
napis += word[-1]

print(napis)