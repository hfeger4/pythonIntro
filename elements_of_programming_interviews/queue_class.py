class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0 ,item)

    def dequeue(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

groceries = Queue()
print(groceries.isEmpty())
groceries.enqueue("grass")
print(groceries.items)
groceries.enqueue("turtles")
groceries.dequeue()
print(groceries.items)
print(groceries.size())




