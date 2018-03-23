class DoublyLinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

a = DoublyLinkedListNode("a")
b = DoublyLinkedListNode("b")
c = DoublyLinkedListNode("c")

a.next = b
b.prev = a
b.next = c
c.prev = b

print(a.value)
print(a.next.value)
print(b.value)
print(b.next.value)
print(c.next.value)