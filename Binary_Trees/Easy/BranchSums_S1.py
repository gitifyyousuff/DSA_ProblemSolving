# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#O(n) T|O(n) S
#It won't run here. #algoexpert
def branchSums(root):
    sums = []
    CalculateBranchSums(root,0,sums)
    return sums
    


def CalculateBranchSums(node,running_sum,sums):
   if node is None:
       return 
   sum_valu = running_sum+node.value
   if node.left is None and node.right is None:
       sums.append(sum_valu)
       return
   CalculateBranchSums(node.left,sum_valu,sums)
   CalculateBranchSums(node.right,sum_valu,sums)