class Queue2Stacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):
        self.stack1.append(item)

    def dequeue(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack2.pop()
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

test = Queue2Stacks()

test.enqueue("howie")
test.enqueue("dude")
test.enqueue("blatant")
print(test.stack1)
test.dequeue()
print(test.stack1)