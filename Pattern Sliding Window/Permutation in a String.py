'''
Problem Challenge 1
Permutation in a String (hard) 
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''

def find_permutation(s,p):
  p_d={}
  for w in p:
    if w not in p_d:
      p_d[w]=0
    p_d[w]+=1
  windowStart=0
  matched=0
  res=[]
  for windowEnd in range(len(s)):
    if s[windowEnd] in p_d:
      p_d[s[windowEnd]]-=1
      if p_d[s[windowEnd]]==0:
        matched+=1
    if matched == len(p_d):
      return True
    if windowEnd-windowStart+1>=len(p_d):
      if s[windowStart] in p_d:
        print(p_d[s[windowStart]])
        if p_d[s[windowStart]]==0:
          matched-=1
        p_d[s[windowStart]]+=1
      windowStart+=1     
  return False

print(find_permutation('oidbcaf','abc'))
print(find_permutation('odicf','dc'))
print(find_permutation('bcdxabcdy','bcdyabcdx'))
print(find_permutation('aaacb','abc'))

'''
Time Complexity:
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity:
The space complexity of the algorithm is O(M) since in the worst case, 
the whole pattern can have distinct characters which will go into the HashMap.
'''
