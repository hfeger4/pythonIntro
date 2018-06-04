class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def removeKFromList(l,k):
    prev = None
    current = l

    while current.nextnode:
        if current.value == k:
            prev.nextnode = current.nextnode

        prev = current
        current = current.nextnode

    return l

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d
#print
print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)


print("Lets remove that element")
removeKFromList(a,3)
print(a.value)
print(a.nextnode.value)
print(b.nextnode.value)
print(c.nextnode.value)
