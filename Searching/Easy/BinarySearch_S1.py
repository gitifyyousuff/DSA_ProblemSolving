#O(log(n))T|O(1)S
def binarySearch(array, target):
    left  = 0
    right = len(array)-1
    while left<=right:
        mid = (left+right)//2
        if target<array[mid]:
            right = mid-1
        elif target>array[mid]:
            left = mid+1
        elif target==array[mid]:
            return mid
    
    return -1

array= [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target=  71

binarySearch = binarySearch(array, target)
print(binarySearch)