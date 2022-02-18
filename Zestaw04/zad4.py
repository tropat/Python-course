def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib1 = 0
    fib2 = 1

    for i in range(2,n+1):
        pom = fib1
        fib1 = fib2
        fib2 = pom + fib1

    return fib2

n = input("n=")
print(fibonacci((int)(n)))