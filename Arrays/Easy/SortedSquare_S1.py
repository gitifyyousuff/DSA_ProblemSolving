def sortedSquaredArray(array):
	sorted_sq = []
	
	for idx in range(len(array)):
		value = array[idx]
		sorted_val = value * value
		sorted_sq.append(sorted_val)
		
	sorted_sq.sort()
	return sorted_sq

sorted_squ = sortedSquaredArray([1,4,6])
print(sorted_squ)