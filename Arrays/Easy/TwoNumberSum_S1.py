#O(n^2) T |O(1)S
def twoNumberSum(array,target):
    for i in range(len(array)-1):
        fn = array[i]
        for j in range(i+1,len(array)):
            sn = array[j]
            if fn+sn == target:
                return [fn,sn]

    return []
#input data below
array=[3, 5, -4, 8, 11, 1, -1, 6]
target =19
two_numbers = twoNumberSum(array,target)
print(two_numbers)
 