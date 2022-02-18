def factorial(n):
    wynik = 1
    for i in range(0,n):
        wynik *= i + 1
    return wynik

print(factorial(5))