#could not run the program - AlgoExpert
#O(log(n))T|O(n)S
#worst:O(n)T|O(n)S
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree,target,float("inf"))
    
def findClosestValueInBstHelper(tree,target,closest):
   if tree is None:
       return closest
   if abs(target-closest)>abs(target-tree.value):
       closest = tree.value
   if target > tree.value:
       return findClosestValueInBstHelper(tree.right,target,closest)
   elif target < tree.value:
       return findClosestValueInBstHelper(tree.left,target,closest)
   else:
    return closest

       


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
