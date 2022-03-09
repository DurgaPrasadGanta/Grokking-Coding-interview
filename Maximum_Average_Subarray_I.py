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
