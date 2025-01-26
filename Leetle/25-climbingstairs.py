'''
Write a function solve that calculates how many distinct ways you can climb a staircase of n steps, taking 1 or 2 steps at a time.

Example:
Input: 3
Output: 3(1+1+1, 1+2, 2+1) 
'''

def solve(n):
    if n <= 1:
        return 1
    return solve(n-1) + solve(n-2)

print(solve(3))

'''
solve(3) = solve(2) + solve(1) = solve(2) + 1
solve(2) = solve(1) + solve(0) = 1 + 1
'''