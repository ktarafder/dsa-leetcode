'''
Write a function solve that finds the length of the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. 
'''

def solve(s):
  prev = set()
  l, res = 0, 0
  for r in range(len(s)):
    while s[r] in prev: # when we reach a duplicate element with our right pointer 
      prev.remove(s[l]) # eleminate all characters to the left of that duplicate including leftmost duplicate
      l += 1
    prev.add(s[r])
    res = max(res, r-l+1)
  return res

print(solve('pwwkew'))

# alternative map based approach
def solve(s):
  mp = {}
  l, res = 0, 0
  for r in range(len(s)):
    if s[r] in mp:
      l = max(mp[s[r]] + 1, l) # if duplicate element move left pointer to element after first occurence of on left to remove duplicate
    mp[s[r]] = r # number and index val of number
    res = max(res, r-l+1) 
  return res

print(solve('pwwkew'))