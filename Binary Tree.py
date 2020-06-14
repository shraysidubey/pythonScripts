#create the Binary Tree.
#Inorder - (Left, Root, Right)
#PostOrder - (Left, Right, Root)
#PreOrder - (Root, Left, Right) 

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def print(self):
        print(self.val, end = " ")

def printInorder(root):
    if root:
        printInorder(root.left)
        
        print(root.val)

        printInorder(root.right)


def printPostOrder(root):
    if root:
        printPostOrder(root.left)

        printPostOrder(root.right)

        print(root.val)
       

def printPreOrder(root):
    if root:
        print(root.val)

        printPreOrder(root.right)

        printPreOrder(root.left)
        
    
root = Node(1)

root.right = Node(2)

root.left = Node(3)

root.left.left = Node(4)

root.left.right = Node(5)

root.right.left = Node(6)

printInorder(root)
print()
printPostOrder(root)
print()
printPreOrder(root)
print()

