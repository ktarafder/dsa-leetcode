from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
    
# Create an instance of the class
sol = Solution()

# Example 1:
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))

# Example 2:
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))

# Line by line output
# nums = [1,2,3,4]
# res = [1,1,1,1]
# prefix, postfix = 1, 1

# First Pass: Calculate Prefix Products
    # i = 0
        # res[0] = prefix = 1
        # prefix *= nums[0] = 1 * 1 = 1

    # i = 1
        # res[1] = prefix = 1
        # prefix *= nums[1] = 1 * 2 = 2

    # i = 2
        # res[2] = prefix = 2
        # prefix *= nums[2] = 2 * 3 = 6

    # i = 3
        # res[3] = prefix = 6
        # prefix *= nums[3] = 6 * 4 = 24 | We don't save this value

    # Final Prefix Order: res = [1, 1, 2, 6]

# Second Pass: Calculate Postfix Products & Final Result
    # i = 3 --> Start from end b/c postfix
        # res[3] *= postfix = 6 * 1 = 6
        # postfix *= nums[3] = 1 * 4 = 4

    # i = 2
        # res[2] *= postfix = 2 * 4 = 8
        # postfix *= nums[2] = 4 * 3 = 12

    # i = 1
        # res[1] *= postfix = 1 * 12 = 12
        # postfix *= nums[1] = 12 * 2 = 24

    # i = 0
        # res[0] *= postfix = 1 * 24 = 24
        # postfix *= nums[0] = 24 * 1 = 24

    # Final Result with both Prefix and Postfix Products:
        # res = [24, 12, 8, 6]

# Time complexity: O(n)
    # The first pass iterates over all the elements which takes O(n) time
    # The second pass iterates backwards over all the elements which takes O(n) time
    # Time complexity = O(n) + O(n) = O(n)

# Space complexity: O(1)
    # We do not use any additional arrays to store prefix and postfix products separately 
        # The result array is reused to store values, so only constant amount of space is used
        # While the output array res grows with the input size, it is not considered extra space since it is necessary to return the result. 
        # Therefore, the space complexity remains O(1).