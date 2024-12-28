# Resource below is pretty good for understanding
# https://leetcode.com/problems/k-radius-subarray-averages/editorial/

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # if k is 0 we just return the nums arr since we're not averaging anything
        if k == 0:
            return nums    
        # since we use len(nums) so much lets just store it in a var
        n = len(nums)
        # noninclusive prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        res = [-1] * n
        radius_size = 2 * k + 1 # k elements to the left, k elements to the right, and + 1 b/c its inclusive of i, this is basically a window
        for i in range(k, n-k): # dont need to look at first k element sums and last k element sums 
            curr = prefix[i+k+1] - prefix[i-k] # right - left
            res[i] = curr // radius_size
        
        return res

# Create an instance of the class
sol = Solution()

# Example 1:
nums, k = [7,4,3,9,1,8,5,2,6], 3
print(sol.getAverages(nums, k))  # [5, 5, 6, 6, 6, 7, 6, 5, -1]
# Example 2:
nums = [100000]
k = 0
print(sol.getAverages(nums, k))  # [100000]

# Sliding Window approach that reduces space complexity down to O(1)
class Solution:
    def getAverages(self, nums, k):
        if k == 0:
            return nums
        
        n = len(nums)
        res = [-1] * n
        window_size = 2 * k + 1

        if window_size > n:
            return res
        
        # first window sum
        curr = sum(nums[:window_size]) # 7,4,3,9,1,8,5
        res[k] = curr // window_size

        for i in range(window_size, n): # i dont get this range, come back to this
            curr = curr - nums[i - window_size] + nums[i]
            res[i-k] = curr // window_size

        return res            


sol2 = Solution()
# Example 1:
nums, k = [7,4,3,9,1,8,5,2,6], 3
print(sol2.getAverages(nums, k))  # [5, 5, 6, 6, 6, 7, 6, 5, -1]