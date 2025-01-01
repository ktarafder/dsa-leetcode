'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''

'''
Normally with subarray problems the first thought that comes to mind is to use a sliding window
Now here we do have a window but its not sliding 
We're going to apply a trick using noninclusive prefix sum & hashing to this problem 
'''

from collections import defaultdict
from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1 # noninclusive prefix sum
    curr, res = 0, 0
    for num in nums:
        curr += num # track prefix sum using integer val
        res += counts[curr - k] # curr - k think about it mathematically we have curr value and we need to subtract some value x to get to k
                                # curr - x = k --> x = curr - k
        counts[curr] += 1 # add current prefix sum to hashmap 
    return res

print(subarraySum([0, 1, 2, 3, 4], 5)) # 1 b/c [2,3] --> 2+3 = 5
print(subarraySum([1, 2, 1, 2, 1], 3)) # 4 b/c [1,2], [2,1], [1,2], [2,1] all sum up to 3
