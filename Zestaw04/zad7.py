def flatten(sequence):
    L = list()
    for el in sequence:
        if isinstance(el, (list, tuple)):
            L.extend(flatten(el))
        else:
            L.append(el)
    return L

L = [2, 5, [2,7, 3, (0, 3)], (1), [4, [3, 1]], 1]
print(L)
print(flatten(L))