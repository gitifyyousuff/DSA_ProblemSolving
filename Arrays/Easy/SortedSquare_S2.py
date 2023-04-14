def sortedSquaredArray(array):
    sq = [num **2 for num in array]
    sq.sort()
    return sq

sorted_squ = sortedSquaredArray([1,4,5])
print(sorted_squ)