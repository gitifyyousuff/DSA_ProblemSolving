#could not run the program - AlgoExpert
#O(log(n))T|O(n)S
#worst:O(n)T|O(n)S
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree,target,float("inf"))
    
def findClosestValueInBstHelper(tree,target,closest):
    current_node = tree
    while current_node is not None:
        if abs(target-closest)>abs(target-current_node.value):
            closest = current_node.value
        if target > current_node.value:
            return findClosestValueInBstHelper(tree.right,target,closest)
        elif target < current_node.value:
            return findClosestValueInBstHelper(tree.left,target,closest)
        else:
            break
    return closest

       


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
