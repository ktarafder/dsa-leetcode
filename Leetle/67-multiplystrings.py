'''
Write a function solve that multiplies two non-negative integers represented as strings.

Example:
Input: "123", "456"
Output: "56088" 
'''

# i missed my python one liners 🥺
def solve(num1: str, num2: str):
  return str(int(num1) * int(num2))

print(solve('123', '456'))