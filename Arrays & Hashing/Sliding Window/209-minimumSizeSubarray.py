from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # We can brute force by comparing each subarray to target 
        # However sliding window is efficient for this problem should run in O(n) time
        # l = 0 curr_sum = 0 (sum of current window) min = float('inf')
        # right pointer that adds to curr_sum until it reaches >= condition
        # Once condition is released first we can check if the current window size is less than the lowest size found so far
        # Update the result if so otherwise keep as is min(res, r - l + 1)
        # remove left pointer value from current sum
        # increment our left pointer
        # return res if exists otherwise return 0

        l = 0
        curr_sum = 0 # sum of elements within window
        res = float('inf')

        for r in range(len(nums)): # expands window size
            curr_sum += nums[r]

            while curr_sum >= target:
                res = min(res, r - l + 1) # compares current window size to that of previous windows that matched condition
                curr_sum -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0

# Time complexity: O(n) where n is the length of the input list
# Space complexity: O(1) as we are only using a few variables to store the result

# Test cases
test = Solution()
print(test.minSubArrayLen(7, [2,3,1,2,4,3]))  # 2
print(test.minSubArrayLen(4, [1,4,4])) # 1
print(test.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0