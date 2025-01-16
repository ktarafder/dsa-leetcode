'''
Write a function solve that finds the length of the longest consecutive sequence in an unsorted list.

Example:
Input: [100,4,200,1,3,2]
Output: 4 
'''

'''
I went with an O(nlogn) sorting approach b/c I couldn't recall the O(n) approach
O(n) approach uses hashset
'''

def solve(nums):
  # edge cases
  if not nums: # no elements
    return 0
  if len(nums) == 1: # only one element
    return 1
  nums = sorted(nums)
  res, curr = 0, 1
  for i in range(len(nums)-1):
    if nums[i+1] == nums[i] + 1:
      curr += 1
    elif nums[i+1] == nums[i]: # [1,1,1,1]
      res = max(res, curr)
      continue
    else:
      curr = 1
    res = max(res, curr)
  return res

print(solve([100,4,200,1,3,2]))

def solve(nums):
    if not nums:
        return 0
    nums = set(nums)
    res = 0
    if len(nums) == 1:
        return 1
    for num in nums:
        if num - 1 not in nums: # if num - 1 not in the hashset that means this number has to be the beginning of a unique sequence 
            curr = num
            streak = 1
        while curr + 1 in nums:
            curr += 1
            streak += 1
        res = max(res, streak)
    return res

print(solve([100,4,200,1,3,2]))
