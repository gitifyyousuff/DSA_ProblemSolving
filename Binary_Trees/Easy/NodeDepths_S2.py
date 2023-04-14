#O(n)T |O(h)S,where h is height of the tree
def nodeDepths(root,sum = 0):
    if root is None:
        return 0
    return sum+nodeDepths(root.left,sum+1)+nodeDepths(root.right,sum+1)
    


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
