'''
Write a function solve that finds the majority element in a list. The majority element appears more than n/2 times where n is the length of the list.
Example:
Input: [3,2,3]
Output: 3 
'''

# First solution 
def solve(nums):
  nums = sorted(nums)
  mid = len(nums) // 2
  return nums[mid]

print(solve([3,2,3]))

# Better solution 
def solve(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)

print(solve([3,2,3]))

# This is the solution I was going for 
from collections import Counter
def solve(nums):
   return max(Counter(nums)) # the issue with this is this returns the max key not the max key value

def solve(nums):
   counts = Counter(nums)
   return max(counts, key=counts.get)

print(solve([3,2,3]))