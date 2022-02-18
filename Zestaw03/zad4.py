x = input("Liczba rzeczywista: ")

while x != "stop":
    try:
        x = (float)(x)
        print(str(x) + " " + str(pow(x, 3)))
    except:
        print("Zle wprowadzonr dane")

    x = input("Liczba rzeczywista: ")