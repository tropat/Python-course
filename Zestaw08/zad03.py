import random

random.seed()

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""

    p = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            p += 1
    return 4 * p / n

print(calc_pi(50))
print(calc_pi())
print(calc_pi(1000))
print(calc_pi(10000))
print(calc_pi(100000))
print(calc_pi(1000000))