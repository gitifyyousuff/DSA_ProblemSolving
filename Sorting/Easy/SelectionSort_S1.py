#O(n^2)T|O(1)S
def SelectionSort(array):
    current_idx = 0
    while current_idx<len(array)-1:
        min_idx = current_idx
        for i in range(current_idx+1,len(array)):
            if array[i]<array[min_idx]:
                min_idx = i
        array[current_idx],array[min_idx] = array[min_idx],array[current_idx]
        current_idx += 1
    return array







array =  [8, 5, 2, 9, 5, 6, 3]
SelectionSort = SelectionSort(array)
print(SelectionSort)