class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def count_leafs(top): 
    if top is None:
        return
    count = 0
    stack = list()  
    stack.append(top)
    while stack:
        node = stack.pop()
        if node.left == None and node.right == None:
            count += 1
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count

def count_total(top): 
    if top is None:
        return
    count = 0
    stack = list()  
    stack.append(top)
    while stack:
        node = stack.pop()
        count += node.data
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return count

top = Node(1, Node(2, Node(3), Node(4, Node(5))), Node(6))
print(count_leafs(top))
print(count_total(top))