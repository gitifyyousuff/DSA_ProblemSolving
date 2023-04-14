# O(n^2)T|O(1)S
def bubbleSort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]> array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
array=  [8, 5, 2, 9, 5, 6, 3]
bubbleSort = bubbleSort(array)
print(bubbleSort)