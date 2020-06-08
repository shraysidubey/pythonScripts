#Stack using the LinkedList.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def appendHaed(self,new_data):
        new_node = Node(new_data)                    #create the new node 370__--> head
        new_node.next = self.head
        self.head = new_node                         #New_node Link to head 

    def deleteHead(self):          
        if self.head is None:
            print("Head is not in the LinkedList")
            return
        self.head = self.head.next

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printList(self):
        temp = self.head
        while(temp!= None):
            print(str(temp.data) + "-->", end = " ")
            temp = temp.next
        return
    print()

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, item):
        self.list.appendHaed(item)
        return self.list
    
    def pop(self):
        if self.list.isEmpty():
            print("Stack is empty")
        else:
            self.list.deleteHead()
            
    def printStack(self):
        self.list.printList()


L = Stack()
print("-------")
L.push("1")
L.printStack()
print("-------")
L.push("w")
L.printStack()
print("-------")
L.push("r")
L.printStack()
print("-------")
L.push("j")
L.printStack()
print("-------")
L.push("t")
L.printStack()
print("-------")
L.pop()
L.printStack()
print("-------")
L.pop()
L.printStack()
L.pop()
L.printStack()
#print(L.list.head.data)



