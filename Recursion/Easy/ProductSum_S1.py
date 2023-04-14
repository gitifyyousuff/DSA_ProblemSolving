
#O(n)T|O(D) S
"""where n is the total elements including single and list elements and list
inside a list.for eg ..given input is 12 elements
O(D) is depth of the array elements, since it is recursion"""
def productSum(array,multiplier = 1):
    sum = 0
    for i in array:
        if type(i) is int:
            sum += i
        else:
            sum += productSum(i,multiplier+1)     
    return sum*multiplier




array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
ProductSum = productSum(array)
print(ProductSum)