n = input("Podaj liczbe: ")
outputUpper = ""
outputLower = ""
output = ""

for i in range((int)(n)+1):
    if i == (int)(n):
        outputUpper += "|"
    else:
        outputUpper += "|...."
    if i == 0:
        outputLower += str(i)
    else:
        outputLower += ((str(i)).rjust(5))

output = outputUpper + "\n" + outputLower

print(output)