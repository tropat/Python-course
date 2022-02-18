x = input("x=")
y = input("y=")

x = (int)(x)
y = (int)(y)

drawing = ""

for i in range(0, 2*y+1):
    for j in range(0, x+1):
        if i % 2 == 0:
            if j != x:
                drawing += "+---"
            else:
                drawing += "+"
        else:
            if j != x:
                drawing += "|   "
            else:
                drawing += "|"
    drawing += "\n"
    
print(drawing)