#O(log(n))T|O(1)S
def binarySearch(array, target):
    return binarySearchHelper(array,target,0,len(array)-1)

def binarySearchHelper(array,target,left,right):
    if left>right:
        return -1
    mid = (left+right)//2
    potential_match = array[mid]
    if target == potential_match:
        return mid
    elif target<potential_match:
        return binarySearchHelper(array,target,left,mid-1)
    elif target>potential_match:
        return binarySearchHelper(array,target,mid+1,right)
    
array= [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target=  71

binarySearch = binarySearch(array, target)
print(binarySearch)