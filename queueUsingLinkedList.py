#create the Queue using the Linkedlist.
class Node:                                                 #enqueue// dequeue // isEmpty// Size// 
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.rear = self.front = None

    def enqueue(self,item):
        if self.rear is None:
            self.rear = self.front = Node(item)
        else:
            new_node = Node(item)
            self.rear.next = new_node
            self.rear = new_node
        return

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front == self.rear:
            self.rear = self.front = None
        else:
            self.front = self.front.next 
        

    def isEmpty(self):
        if self.rear is None:
            return True
        else:
            return False

    def getFront(self):
        if self.front is None:
            print("Queue is none")
            return self.front
        else:
            return self.front.data

    def size(self):
        count = 0
        temp = self.front
        while True:
            if temp != None:
                temp = temp.next
                count = count + 1
            else:
                break
        return count
    

    def print(self):
        temp = self.front
        while True:
            if temp != None:
                print(temp.data,end = " ")
                temp = temp.next
            else:
                break
        print()
        

q = Queue()

S = q.size()
print(S)

q.enqueue(10)
q.print()

q.enqueue(100)
q.print()

q.enqueue(1000)
q.print()

q.enqueue(510)
q.print()

q.enqueue(130)
q.print()

S = q.getFront()
print(S)

q.dequeue()
q.print()

print(q.getFront())

