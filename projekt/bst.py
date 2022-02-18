#!/usr/bin/python

from node import *
import math

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.root == None

    def insert_rek(self, node, prev, val):
        if node is None:
            self.size += 1
            return Node(data=val,parent=prev)
        else:
            if node.data == val:
                return node
            elif node.data < val:
                node.right = self.insert_rek(node.right, node, val)
            else:
                node.left = self.insert_rek(node.left,node, val)
        return node

    def insert(self,val):
        self.root = self.insert_rek(self.root,None,val)

    def inorder_rek(self,node):
        if node != None:
            self.inorder_rek(node.left)
            print("Node: " + str(node.data) + " Parent: " + str(node.parent))
            #print(node.data)
            self.inorder_rek(node.right)
    
    def inorder(self):
        self.inorder_rek(self.root)

    def minValue(self, node):
        tmp = node
        while(tmp.left != None):
            tmp = tmp.left
        return tmp

    def delete_rek(self, node, val):
        if node == None:
            return node

        if val < node.data:
            node.left = self.delete_rek(node.left, val)
            if node.left != None:
                node.left.parent = node
        elif val > node.data:
            node.right = self.delete_rek(node.right, val)
            if node.right != None:
                node.right.parent = node
        else:
            if node.left == None:
                tmp = node.right
                node = None
                return tmp
            elif node.right == None:
                tmp = node.left
                node = None
                return tmp

            tmp = self.minValue(node.right)
            node.data = tmp.data
            node.right = self.delete_rek(node.right, tmp.data)

        return node

    def delete(self,val):
        self.root = self.delete_rek(self.root,val)

    def search_rek(self, node, val):
        if node == None or node.data == val:
            return node
        if node.data < val:
            return self.search_rek(node.right,val)
        return self.search_rek(node.left,val)

    def search(self,val):
        return self.search_rek(self.root,val)
        
    def tree_to_vine(self,root):
        tail = root
        rest = tail.right
        while rest != None:
            if rest.left == None:
                tail = rest
                rest = rest.right
            else:
                temp = rest.left
                rest.left = temp.right
                temp.right = rest
                rest = temp
                tail.right = temp
        return root

    def vine_to_tree(self,root, size):
        leaves = size + 1 - int(math.pow(2,math.floor(math.log2(size+1))))
        root = self.compress(root,leaves)
        size = size - leaves
        while size > 1:
            root = self.compress(root,size//2)
            size = size // 2
        return root

    def compress(self, root, count):
        scanner = root
        for i in range(0,count):
            prev = scanner
            child = scanner.right
            scanner.right = child.right
            scanner = scanner.right
            child.right = scanner.left
            if child.right != None:
                child.right.parent = child
            scanner.left = child
            if scanner.left != None:
                scanner.left.parent = scanner
            scanner.parent = prev
        return root

    def dsw(self):
        pseudoRoot = Node()
        pseudoRoot.right = self.root
        pseudoRoot = self.tree_to_vine(pseudoRoot)
        pseudoRoot = self.vine_to_tree(pseudoRoot,self.size)
        self.root = pseudoRoot.right
        self.root.parent = None

    def reset(self):
        self.size = 0
        self.root = None