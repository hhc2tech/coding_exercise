class Node(object):
    """docstring for Node"""
    def __init__(self, key):
        self.val = key 
        self.left = None 
        self.right = None 

def printInorder(root):
    if root: 
        printInorder(root.left)
        print root.val,
        printInorder(root.right)

def printPreorder(root):
    '''
    (root, left, right)
    '''
    if root: 
        print root.val, 
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    '''
    ( left, right, root)
    '''
    if root: 
        printPostorder(root.left)
        printPostorder(root.right)
        print root.val, 


# def print
root = Node(1) 
root.left = Node(2)
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print "Inorder traversal of binary tree is"
printInorder(root)
print "\nPreorder traversal of binary tree is"
printPreorder(root)
        

print "\nPostorder traversal of binary tree is"
printPostorder(root)
        