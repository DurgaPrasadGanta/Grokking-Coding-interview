'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

def totalFruit(fruits):
  res=0
  fruits_dict={}
  windowStart=0
  for windowEnd in range(len(fruits)):
    f1=fruits[windowEnd]
    if f1 not in fruits_dict:
      fruits_dict[f1]=1
    else:
      fruits_dict[f1]+=1
    while(len(fruits_dict)>2):
      f2=fruits[windowStart]
      fruits_dict[f2]-=1
      if fruits_dict[f2]==0:
        del fruits_dict[f2]
      windowStart+=1
    res=max(res,windowEnd-windowStart+1)
  return res

fruits = ['A', 'B', 'C', 'A', 'C']
print(totalFruit(fruits))


'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input array. 
The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N)which is asymptotically equivalent to O(N).

Space Complexity 
The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.

Similar Problems 
Problem 1: Longest Substring with at most 2 distinct characters
Given a string, find the length of the longest substring in it with at most two distinct characters.
Solution: This problem is exactly similar to our parent problem.
'''
