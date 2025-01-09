'''
Write a function solve that finds two numbers in a list that add up to a target value. Return a list with their indices in order. If the target cannot be made, return an empty list.

Example:
Input: [2, 7, 11, 15], target=9
Output: [0, 1] 
'''

'''
Solving two sum is refreshing, it's crazy to think there was a time where I couldn't solve this problem
Even after I learned how to solve it I would struggle on it a couple times afterwards, but not I feel I can implement it in my sleep lol 
'''

def solve(nums, target):
  map = {}
  for i in range(len(nums)):
    diff = target - nums[i]
    if diff in map:
      return [map[diff], i]
    map[nums[i]] = i
  return []

# Solution on leetle
def solve(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
              