def make_ruler(n):
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

    return output

def make_grid(rows, cols):
    drawing = ""

    for i in range(0, 2*rows+1):
        for j in range(0, cols+1):
            if i % 2 == 0:
                if j != cols:
                    drawing += "+---"
                else:
                    drawing += "+"
            else:
                if j != cols:
                    drawing += "|   "
                else:
                    drawing += "|"
        drawing += "\n"

    return drawing

print(make_ruler(6))
print('\n' + make_grid(4,5))