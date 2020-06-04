#creation of the Linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def appendLastNode(head, new_data):
    temp = head
    new_node = Node(new_data)          #create the new node 
    while(temp.next != None):          #iterate over the LinkedList
        temp = temp.next               #when it comes to last temp ,temp.next == none  condition become false 
    temp.next = new_node               #come out of loop add to the last node 
    
def appendFirstNode(head, new_data):
    new_node = Node(new_data)           #create the new node 370__--> head
    new_node.next = head                #New_node Link to head 
    return new_node                     

def appendInMiddle(head,new_data,key):
    temp = head                          
    while(temp != None and temp.data != key):       #when the key become equals condition become false
        temp = temp.next
    if temp is None:
        print("did't find the key in the LinkedList")
        return
    new_node = Node(new_data)               #550(create the new_node)
    new_node.next = temp.next               #550-->2 1.new_node Link with the its next node
    temp.next = new_node                    #previous node link with the new_node

def deleteSelectedNode(head, key):
    if head == None:                        # check if head is not in the list
        print("Head is not in the LinkedList")
    if head.data == key:                    #key of head is equal to key
        head = head.next 
        return head
    prev = head                            
    temp = head.next                #initialize 
    while True:                     #iterate 
        if temp is None:            #check if there is no temp in linked list
            print(" kghkhh")
            return head
        if temp.data == key:        #if data of temp become equal to key
            prev.next = temp.next   #this will skip the selected key of node
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
        if temp.next.next == None:          #if next of next of node is none codition becomes true 
            temp.next = None                #and that next of temp become none
            break
        temp = temp.next                    #pointing to the every next node in Link list
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
