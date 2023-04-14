def isMonotonic(array):
    isUpward = True
    isDownward = True
    for i in range(1,len(array)):
        if array[i] > array [i-1]:
            isDownward = False
        if array[i]< array[i-1]:
            isUpward = False
    return isUpward or isDownward

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
isMonotonic = isMonotonic(array)
print(isMonotonic)