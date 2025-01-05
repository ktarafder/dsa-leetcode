'''
Write a function solve that finds the missing number in a list of numbers from 0 to n. The list is missing one number.

Example:
Input: [3,0,1]
Output: 2 
'''

'''
I've solved this before it's leetcode problem 268. Was able to get an efficient O(n) time and O(1) space solution in 40 seconds
using the summation formula. Now that I know about XOR thanks to 2. Single Element it can also be applied here for same complexities
'''

def solve(nums):
  n = len(nums)
  expected = n * (n+1) // 2
  return expected - sum(nums)

print(solve([3,0,1]))

def solve(nums):
  res = 0
  for i, num in enumerate(nums):
    res ^= i ^ num
  return res ^ len(nums)

print(solve([3,0,1]))

'''
Dry run of XOR approach
res ^ i ^ nums
i, num
0, 3
0 ^ 0 = 0 -> 0 ^ 3 = 3

i, num
1, 0
3 ^ 1 = 2 -> 2 ^ 0 = 2

i, num
2, 1
2 ^ 2 = 0 ^ 1 = 1

res ^ len(nums)
1 ^ 3 = 2
'''