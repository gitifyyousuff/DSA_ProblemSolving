# O(n)T|O(n)S
def twoNumberSum(array, targetSum):
	nums = {}
	for num in array:
		pm = targetSum-num
		if pm in nums:
			return[pm,num]
		else:
			nums[num]=True
			
	return []


array=[3, 5, -4, 8, 11, 1, -1, 6]
target =19
two_numbers = twoNumberSum(array,target)
print(two_numbers)
 