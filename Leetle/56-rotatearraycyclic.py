'''
Write a function solve that rotates an array to the right by k steps. Ideally, you should be able to rotate the array in-place, but be sure to still return your solution.

Example:
Input: [1,2,3,4,5,6,7], 3
Output: [5,6,7,1,2,3,4] 
'''

# 0 indexed array 
def solve(nums, k):
  n = len(nums)
  k = k % n # dont repeat rotations
# in place  # inclusive    # exclusive
  nums[:] = nums[n - k:] + nums[:n - k]
  return nums

print(solve([1,2,3,4,5,6,7], 3))