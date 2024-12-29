from typing import List 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # fun math solution
        n = len(nums)
        expected_sum = n * (n+1) // 2
        return expected_sum - sum(nums)
    
sol = Solution()
print(sol.missingNumber([3,0,1])) # 2
print(sol.missingNumber([0,1])) # 2

# Could also use a hashset approach here 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashset = set(nums)
        for i in range(len(nums)+1): # plus 1 because we currently have n-1 numbers and need to reach n numbers: n+1 nums
            if i not in hashset:
                return i
    
sol = Solution()
print(sol.missingNumber([3,0,1])) # 2
print(sol.missingNumber([0,1])) # 2