from bst import *

b = BinarySearchTree()

print("Is empty: " + str(b.is_empty()))

b.insert(1)
b.insert(2)
b.insert(-3)
b.insert(10)
b.insert(-1)
b.insert(-7)
b.insert(7)
b.insert(11)
b.insert(9)
b.insert(-10)
b.insert(-11)
b.insert(-12)

print("\nNot balanced tree:\n")
b.inorder()

print("\nIs empty: " + str(b.is_empty()))

print("\nDelete 2: \n")
b.delete(2)
b.inorder()

print("\nSearch 2: ")
print(b.search(2))
print("\nSearch 1: ")
print(b.search(1))

print("\nTree balanced with DSW algorithm: \n")
b.dsw()
b.inorder()

print("\nReset tree\n")
b.reset()
print("Is empty: " + str(b.is_empty()))