#O(nlog(n)+mlog(m))T|O(1)S
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxone = 0
    idxtwo = 0
    smallest = []
    current = float('inf')
    small = float('inf')
    while idxone < len(arrayOne) and idxtwo < len(arrayTwo):
        first_num = arrayOne[idxone]
        second_num = arrayTwo[idxtwo]
        current = abs(first_num-second_num)
        if first_num < second_num:
            idxone += 1
        elif first_num > second_num:
            idxtwo += 1
        else:
            return [first_num,second_num]
        
        if current < small:
            small = current
            smallest = [first_num,second_num] 

    return smallest

arrayOne =  [-1, 5, 10, 20, 28, 3]
arrayTwo =  [26, 134, 135, 15, 17]
smallestDifference = smallestDifference(arrayOne, arrayTwo)
print(smallestDifference)