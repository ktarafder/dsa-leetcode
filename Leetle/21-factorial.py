'''
Write a function solve that returns the factorial of a given integer n. Return 1 if n is 0. 
'''

'''
recursion starting to make a lot of sense compared to a year ago
'''

def solve(n):
  if n == 0:
    return 1
  return n * solve(n-1) 

print(solve(5)) # 5! = 5 * 4 * 3 * 2 * 1 = 120

# Iterative Factorial
def solve(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(solve(5)) # 5! = 5 * 4 * 3 * 2 * 1 = 120