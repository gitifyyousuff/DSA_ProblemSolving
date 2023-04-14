# O(n^2)T|O(n)
def threeNumberSum(array, targetSum):
    array.sort()
    threeNumberList = []
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left < right:
            three_sum = array[i]+array[left]+array[right]
            if three_sum == targetSum:
                threeNumberList.append([array[i],array[left],array[right]])
                left += 1
                right -= 1
            elif three_sum > targetSum:
                right -= 1
            else:
                left += 1
    return threeNumberList       




array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
targetSum = 18
threeNumberSum = threeNumberSum(array, targetSum)
print(threeNumberSum)