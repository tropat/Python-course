slownik = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

#slownik = dict([("I", 1), ("V", 5), ...])
#slownik = dict(zip(["I", "V", ...], [1, 5, ...]))
#slownik = dict(I=1, V=5, ...)

def roman2int(roman):
    liczba = 0
    if len(roman) != 0:
        for i in range(0, len(roman)):
            if i!= len(roman)-1 and slownik[roman[i]] < slownik[roman[i+1]]:
                liczba -= slownik[roman[i]]
            else:
                liczba += slownik[roman[i]]
    return liczba

print("MCMLVI" + " - " + str(roman2int("MCMLVI")))