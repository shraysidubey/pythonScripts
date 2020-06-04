#creation of the Linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def appendLastNode(head, new_data):
    temp = head
    new_node = Node(new_data)          #3
    while(temp.next != None):          #true
        temp = temp.next               #when it comes to last temp ,temp.next == none  condition become false 
    temp.next = new_node
    
def appendFirstNode(head, new_data):
    new_node = Node(new_data)           #370__--> head
    new_node.next = head                 
    return new_node

def appendInMiddle(head,new_data,key):
    temp = head
    while(temp != None and temp.data != key):
        temp = temp.next
    if temp is None:
        print("did't find the key in the LinkedList")
        return
    new_node = Node(new_data)                   #550
    new_node.next = temp.next                #550-->2
    temp.next = new_node

def deleteSelectedNode(head, key):
    if head == None:
        print("Head is not in the LinkedList")
    if head.data == key:
        head = head.next 
        return head
    prev = head
    temp = head.next
    while True:
        if temp is None:
            print(" kghkhh")
            return head
        if temp.data == key:
            prev.next = temp.next
            break
        prev = prev.next
        temp = temp.next
    return head
        

def deleteHead(head):          
    if head is None:
        print("Head is not in the LinkedList")
        return
    #head = head.next
    #return head
    return head.next

def deleteLastNode(head):
    temp = head
    if head is None:
        print("Head is not in the LinkedList")
        return
    while True:
        if temp.next.next == None:
            temp.next = None
            break
        temp = temp.next
    return

def printList(head):
    temp = head
    while(temp != None):
        print(str(temp.data) + " --> ",end = " ")
        temp = temp.next
    print()


head = None

node1 = Node(1)     
head = node1
	
node2 = Node(2)
head.next = node2
	
node3 = Node(3)
node3.next = head
head = node3

appendLastNode(head,10)
printList(head)

appendLastNode(head,100)
printList(head)

appendLastNode(head,800)
printList(head)

appendInMiddle(head,555,800)
printList(head)

head = appendFirstNode(head,750)
printList(head)

head = deleteHead(head)
printList(head)

deleteLastNode(head)
printList(head)

head = deleteSelectedNode(head,-2)
printList(head)
