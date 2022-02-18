
class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_tail(self):        # klasy O(n)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.tail
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            n = self.head
            while n != None:
                if n.next == self.tail:
                    n.next = None
                    self.tail = n
                n = n.next
        
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def join(self, other):    # klasy O(1)
        if self.is_empty():
            self.head = other.head
        else:
            self.tail.next = other.head

        self.tail = other.tail
        self.length += other.length
        other.head = None
        other.tail = None
        other.length = 0

    def clear(self):      # czyszczenie listy
        self.head = None
        self.tail = None
        self.length = 0

lista1 = SingleList()
lista2 = SingleList()

lista1.insert_head(Node(1, None))
lista1.insert_head(Node(2, None))
lista1.insert_head(Node(3, None))
lista1.insert_head(Node(4, None))
lista1.insert_tail(Node(5, None))

lista2.insert_head(Node(7, None))
lista2.insert_head(Node(9, None))

print("Lista1 - head, tail:")
print(lista1.head)
print(lista1.tail)
print("Lista2 - head, tail:")
print(lista2.head)
print(lista2.tail)

print("Lista1 - remove tail")
print(lista1.remove_tail())
print("Lista1 - tail")
print(lista1.tail)

lista1.join(lista2)
print("Lista1 - head, tail:")
print(lista1.head)
print(lista1.tail)
print("Lista2 - head, tail:")
print(lista2.head)
print(lista2.tail)