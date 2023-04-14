def findThreeLargestNumbers(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]  
        

    return array[-3::]






array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
findThreeLargestNumbers = findThreeLargestNumbers(array)
print(findThreeLargestNumbers)