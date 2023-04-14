# O(n log(n))T|O(1)S
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right :
        cs = array[left]+array[right]
        if cs == targetSum:
            return[array[left],array[right]]
        elif cs < targetSum:
            left+=1
        elif cs > targetSum:
            right-=1
        
    return []

array=[3, 5, -4, 8, 11, 1, -1, 6]
targetSum =19
two_numbers = twoNumberSum(array,targetSum)
print(two_numbers)
 