class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def intersection(list1,list2):
    p,q = list1,list2
    while p != q:
        p = p.next if p else list2
        q = q.next if q else list2
    return p

def union_list(list1,list2):
    return

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c

a2 = Node("a")
b2 = Node("c")
d2 = Node("d")

a2.next = b2
b2.next = d2

print(intersection(a,a2))