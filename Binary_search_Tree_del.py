class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def insert(root,node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def getMinVal(root):
    if root.left is None:
        return root.data
    else:
        return getMinVal(root.left) 
    
def deleteNode(root,data):
    if root is None:
        return root
    if root.data == data:
        if root.left == None and root.right == None:
            return None
        elif root.left == None and root.right != None:
            return root.right
        elif root.left != None and root.right == None:
            return root.left
        else:
            min_val = getMinVal(root.right)
            print(min_val)
            root.data = min_val
            root.right = deleteNode(root.right,min_val)
            return root
        
    if data < root.data:
        root.left = deleteNode(root.left,data)
    elif data > root.data:
        root.right = deleteNode(root.right,data)
    return root
        
    
r = Node(11)

insert(r,Node(6))

insert(r,Node(19))

insert(r,Node(4))

insert(r,Node(8))

insert(r,Node(17))

insert(r,Node(43))

insert(r,Node(5))

insert(r,Node(31))

insert(r,Node(49))

deleteNode(r,19)
inOrder(r)

