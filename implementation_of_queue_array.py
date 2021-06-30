class Queue:
    def __init__(self):
        self.L = [None]*10
        self.front = -1
        self.rear = -1
        self.size = 10

    def emqueue(self, ele):
        if self.rear == self.size -1:
            print "overflow"
            return
        else:
            self.rear = self.rear+1
            self.L[self.rear] = ele
            print "list", self.L
            return ele

    def dequeue(self):
        if self.rear == -1:
            return
        else:
            self.front = self.front +1
            
        
    def is_full(self):
        if self.rear == -1:
            print "Underflow"
            return
        else:
            print "kjbcifnijenr"
        
    def is_empty(self):
        if self.rear == -1 and self.front == -1:
            print "list is empty"
            return
                    
    def top(self):
        return self.L[self.front]

K = Queue()
A = K.emqueue("2")
A = K.emqueue("10")
A = K.emqueue("288")
A = K.emqueue("29")
A = K.emqueue("22")
A = K.emqueue("200")
A = K.emqueue("22")
A = K.emqueue("29")


print A

A = K.top()
print A

print "-------------------"
K.dequeue()
print "-------------------"
K.dequeue()
K.dequeue()
K.dequeue()
K.dequeue()
K.dequeue()
K.dequeue()
K.dequeue()
K.dequeue()
K.dequeue()
A = K.top()
print A

print "888888888888888888888"
K.is_full()
print "888888888888888888888"

K.is_empty()
















              

