def sum_seq(sequence):
    sum=0
    for el in sequence:
        if isinstance(el, (list, tuple)):
            sum += sum_seq(el)
        else:
            sum += el
    return sum

L = [2, 4, [9, 1, 5,(1)], 7, (2, 6), [8], 1]
print(sum_seq(L))