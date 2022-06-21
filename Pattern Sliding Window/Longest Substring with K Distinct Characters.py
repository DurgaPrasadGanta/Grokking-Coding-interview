'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''

def longest_substring_with_k_distinct(s,K):
  windowStart=0
  res=0
  char_freq={}
  for windowEnd in range(len(s)):
    c1=s[windowEnd]
    if c1 not in char_freq:
      char_freq[c1]=0
    char_freq[c1]+=1
    while len(char_freq)>K:
      c2=s[windowStart]
      char_freq[c2]-=1
      if char_freq[c2]==0:
        del char_freq[c2]
      windowStart+=1
    res=max(res,windowEnd-windowStart+1)
  return res

print(longest_substring_with_k_distinct('araaci',2))
print(longest_substring_with_k_distinct('araaci',1))
print(longest_substring_with_k_distinct('cbbebi',3))

'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string. 
The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).

Space Complexity 
The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
'''
