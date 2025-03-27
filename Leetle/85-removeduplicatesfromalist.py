"""
Write a function solve that removes duplicates from a list while preserving the original order.

Example:
Input: [1, 2, 2, 3, 4, 4]
Output: [1, 2, 3, 4] 
"""

def solve(arr):
  seen = set()
  res = []
  for i in range(len(arr)):
    if arr[i] not in seen:
      seen.add(arr[i])
      res.append(arr[i])
  return res

print(solve([1,2,2,3,4,4]))

