'''
Write a function solve that finds the maximum of three numbers.

Example:
Input: (3, 7, 5)
Output: 7 
'''

'''
yay leetle has js now, so I can suffer in both python and js 🫠
'''

def solve(a, b, c):
    return max(a,b,c)

print(solve(1,2,3))

# Javascript solution
'''
function solve(a, b, c) {
  return Math.max(a, b, c)
}
'''

# This cool thing should run in node.js 
lambda: eval("function solve(a, b, c) { return Math.max(a, b, c) } console.log(solve(1,2,3))")