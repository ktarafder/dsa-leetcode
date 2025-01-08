'''
Write a function solve that determines if a string s of parentheses is valid. Valid parentheses must be closed in the correct order.

Example:
Input: "()[]{}"
Output: True 
'''

'''
Thank god we're thrown an easy one today that unfortunately I have memorized from my DSA class days
If I hadn't prlly wouldn't be able to solve, I need to do more stack problems
I'm not even writing the tests for these ones, if you have an issue with it how about you stack these ... nvm
'''

def solve(s):
  stack = []
  parentheses_map = {')':'(', '}':'{', ']':'['}
  for c in s:
    if c in parentheses_map:
      if stack and stack[-1] == parentheses_map[c]:
        stack.pop()
      else:
        return False
    else:
      stack.append(c)
  return True if not stack else False

# leetle solution
def solve(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{': stack.append(c)
        elif not stack or stack.pop() != pairs[c]: return False
    return len(stack) == 0
              