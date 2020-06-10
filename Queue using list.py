#Implementation of Queue using List
class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self,item):
        self.list.append(item)
        return self.list

    def dequeue(self):
        self.list.pop(0)
        return self.list

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.list)
    

q = Queue()
S = q.enqueue(10)
S = q.enqueue(20)
S = q.enqueue(30)
S = q.enqueue(40)
S = q.enqueue(50)
S = q.dequeue()
print(S)
S = q.isEmpty()
print(S)
S = q.size()
print(S)

