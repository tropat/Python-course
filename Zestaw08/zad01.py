def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b != 0:
        print("x - dowolna liczba rzeczywista, y = " + str(-c/b))
    elif a != 0 and b == 0:
        print("x = " + str(-c/a) + ", y - dowolna liczba rzeczywista")
    elif a == 0 and b == 0 and c == 0:
        print("x, y - dowolne liczby rzeczywiste")
    elif a == 0 and b == 0 and c != 0:
        print("rownanie sprzeczne")
    else:
        print("y = " + str(-c/b) + " + (" + str(-a/b) + ")x")

