'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example: 1
nums=[2, 3, 4, 1, 5], k=2
output: 7

Example:2
nums=[2, 1, 5, 1, 3, 2], k=3
output: 9
'''

def maxSubarrayOfSizeK(nums,k):
  maxSum=0
  s=sum(nums[:k])
  maxSum=s
  for i in range(k,len(nums)):
    s+=nums[i]-nums[i-k]
    if s>maxSum:
      maxSum=s
  return maxSum

print(maxSubarrayOfSizeK([2,3,4,1,5],2))
print(maxSubarrayOfSizeK([2,1,5,1,3,2],3))

'''
Time Complexity: o(n)
Space Complexity: o(1)
'''
