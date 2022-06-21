
'''
Problem Challenge 2
String Anagrams (hard) 
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

def string_Anagrams(s,p):
  p_d={}
  for char in p:
    if char not in p_d:
      p_d[char]=1
    else:
      p_d[char]+=1
  result=[]
  windowStart=0
  matched=0
  for windowEnd in range(len(s)):
    leftChar=s[windowEnd]
    if leftChar in p_d:
      p_d[leftChar]-=1
      if p_d[leftChar]==0:
        matched+=1
    if matched==len(p_d):
      result.append(windowStart)
    if windowEnd-windowStart+1>=len(p_d):
      rightChar=s[windowStart]
      if rightChar in p_d:
        if p_d[rightChar]==0:
          matched-=1
        p_d[rightChar]+=1
      windowStart+=1
  return(result)


print(string_Anagrams('ppqp','pq'))
print(string_Anagrams('abbcabc','abc'))


'''
Time Complexity:
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity: 
The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. 
In the worst case, we also need O(N) space for the result list, this will happen when the pattern has only one character and the string contains only that character.
'''
