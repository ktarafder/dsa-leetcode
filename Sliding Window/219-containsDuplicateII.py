from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True      
            window.add(nums[R])
        return False

# Time complexity: O(n) b/c we're iterating through the entire list
# Space complexity: O(k) where k is the size of the window

# Brute force solution
'''
def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)): # Window can be of size k or less
            if nums[L] == nums[R]:
                return True
    return False
'''