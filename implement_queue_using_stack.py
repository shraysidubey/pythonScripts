class Queue:
    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def enqueue(self, element):
        self.stack.append(element)
        return self.stack

    def dequeue(self):
        if len(self.stack) == 0 and len(self.stack_2) == 0:
            return "Queue is empty"
        while len(self.stack) != 0:
            element = self.stack.pop()
            self.stack_2.append(element)
        val = self.stack_2.pop()

        while len(self.stack_2) != 0:
            element = self.stack_2.pop()
            self.stack.append(element)

        return val


Q = Queue()
print Q.dequeue()
print Q.enqueue(3)
print Q.dequeue()
print Q.enqueue(10)
print Q.enqueue(7)
print Q.enqueue(6)
print Q.dequeue()
print Q.dequeue()
