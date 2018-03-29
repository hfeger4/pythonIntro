class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")

a.next = b
b.next = c

print(a.next.value)

def select_last(head):
    current = head
    while current.next != None:
        current = current.next
        last = current
    print(last.value)

select_last(a)