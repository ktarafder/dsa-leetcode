'''
Write a function solve that reverses a string.

Example:
Input: "hello"
Output: "olleh" 
'''

'''
I immediately thought of s[::-1] but wanted to try implement it with swapping
I failed at first b/c I tried to swap directly without converting s to a list first
    - in python, strings are immutable so you can't swap two chars directly
'''

def solve(s):
  s = list(s)
  l, r = 0, len(s) - 1
  while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1
  return ''.join(s)

print(solve('hello'))