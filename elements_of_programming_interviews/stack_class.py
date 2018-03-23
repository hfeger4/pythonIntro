class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

toys = Stack()

toys.push("Howie")
toys.push("Kimmy")
print(toys.items)
toys.pop()
print(toys.items)
print(toys.peek())
print(toys.size())