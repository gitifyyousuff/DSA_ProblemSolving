# You're given a list of integers nums . Write a function that returns a
#  boolean representing
# whether there exists a zero-sum subarray of [ums .

# A zero-sum subarray is any subarray where all of the values
#  add up to zero. A subarray is any
# contiguous section of the array. 

#O(n)TS
def zeroSumSubarray(nums):
    seen = {0}
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum in seen:
            return True
        seen.add(current_sum)
    return False

nums = [-1, 2, 3, 4, -5, -3,1, 2]
zeroSumSubarray = zeroSumSubarray(nums)
print(zeroSumSubarray)