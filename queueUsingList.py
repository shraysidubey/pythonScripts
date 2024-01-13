#Implementation of Queue using List
class Queue:
    
    def __init__(self):
        self.lst = []

    def enqueue(self, element):
        self.lst.append(element)
        return self.lst
    
    def dequeue(self):
        self.lst.pop(0)
        return self.lst
    
    def front(self):
        return "The front value of the queue " + str(self.lst[0])
    
    def rear(self):
        return "The rear value of the queue " + str(self.lst[len(self.lst)-1])
    
    def size_of_queue(self):
        return "The length of the queue " + str(len(self.lst))
    
    def is_empty(self):
        if len(self.lst) == 0:
            return "The queue is empty"
        else:
            return "The is not empty" + str(self.lst)
        
    def __str__(self) -> str:
        print("The queue is" + str(self.lst))

obj_a = Queue()
obj_a.enqueue("a")
obj_a.enqueue("b")
obj_a.enqueue("c")
obj_a.enqueue("d")
obj_a.enqueue("e")
obj_a.enqueue("g")
obj_a.__str__()
print(obj_a.dequeue())

print(obj_a.front())  #b
print(obj_a.size_of_queue())
obj_a.__str__()

