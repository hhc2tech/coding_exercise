class TreeNode(object):
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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root: 
        #     return max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root, right))

        # return 0:
        def rec(tree):
            if tree:
                l = rec(tree.left)
                r = rec(tree.right)
                depth = 1 + max(l[1], r[1])
                length = max(l[0], r[0], l[1] + r[1])
                return (length, depth)
            return (0, 0)

        return rec(root)





root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(Solution().diameterOfBinaryTree(root))




