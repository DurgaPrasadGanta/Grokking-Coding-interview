
'''
You are given an integer array nums consisting of n elements, and an integer k.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

def findMaxAverage(nums,k):
  maxSum=0
  sum=0
  for i in range(k):
    sum=sum+nums[i]
  maxSum=sum
  for i in range(k,len(nums)):
    sum=sum+nums[i]-nums[i-k]
    if sum>maxSum:
      maxSum=sum
  return (maxSum/k)

'''
Time Complexity: o(n)
Space Complexity: o(1)
'''