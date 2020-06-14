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
        
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))
inOrder(r)
