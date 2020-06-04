#create the stack with the list.
class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
        return

    def pop(self):
        self.list.pop()
        return

    def isempty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
                
    def size(self):
        return len(self.list)

    def top(self):
        if self.isempty():
            return "Stack is empty"
        return self.list[len(self.list)-1]

    def __str__(self):
        return "Elements of Stack are:" + str(self.list)

        
L = Stack()
L.push("a")
L.push("2")
L.push("b")
L.push("3")
print(L)

L.pop()
L.pop()
L.pop()
L.pop()

print(L.list)

S = L.isempty()
print(S)

S = L.size()
print(S)

S = L.top()
print(S)

#C++ has call by value and call by refernce: https://ideone.com/6O0wEO
#Python is call by object reference: https://ideone.com/49lKmm


