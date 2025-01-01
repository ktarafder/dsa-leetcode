from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1 
        curr, res = 0, 0

        for num in nums:
            curr += num % 2 # track odd numbers
            res += counts[curr - k]
            counts[curr] += 1
        return res

sol = Solution()
nums = [1,1,2,1,1]
k = 3
print(sol.numberOfSubarrays(nums, k)) # 2

# stdout
'''
1
0
defaultdict(<class 'int'>, {0: 1, -2: 0, 1: 1})
2
0
defaultdict(<class 'int'>, {0: 1, -2: 0, 1: 1, -1: 0, 2: 1})
2
0
defaultdict(<class 'int'>, {0: 1, -2: 0, 1: 1, -1: 0, 2: 2})
3
1
defaultdict(<class 'int'>, {0: 1, -2: 0, 1: 1, -1: 0, 2: 2, 3: 1})
4
2
defaultdict(<class 'int'>, {0: 1, -2: 0, 1: 1, -1: 0, 2: 2, 3: 1, 4: 1})
2
'''