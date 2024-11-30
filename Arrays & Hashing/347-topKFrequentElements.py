from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # frequency map
        freq = {}
        # bucket
        bucket = [[] for _ in range(len(nums) + 1)]

        # construct freq map
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        # assemble the bucket
        for n, c in freq.items():
            bucket[c].append(n)

        # get top k elements from bucket
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
            if len(res) == k:
                return res

sol = Solution()
# Test cases
print(sol.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(sol.topKFrequent([1], 1))  # [1]

'''
This is a solution I mostly came up with my own
The thing that I got stuck on was how to obtain the greatest frequency element along with key in a dictionary
I found out we can use the iterable freqMap in the max function along with this key argument freqMap.get
freqMap.get will get the values of all the keys in the dictionary 
The max function comapres all the values of the keys and returns the key with the maximum value
This takes O(n) time to find the maximum value in a dictionary where n is the number of keys in the dictionary
And this can occur k times where k is the number of elements we want to find in the dictionary
This gives us a time complexity of O(n * k), which isn't the most efficient solution

Note: The first for loop to construct the freqMap takes O(m) time where m is the number of elements in the input list
However, it becomes insignificant when compared to the time complexity of the max function
So O(m) + O(n * k) = O(n * k)
'''
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap frequency nums 
        freqMap = {}
        res = []
        # iterate through map to build freqMap
        for i in nums:
            freqMap[i] = 1 + freqMap.get(i, 0)
        # Use a loop to find the top k frequent elements
        for _ in range(k):
            # Find the key with the maximum frequency
            maxKey = max(freqMap, key=freqMap.get)
            # add to res
            res.append(maxKey)  
            # remove most frequent key post 
            del freqMap[maxKey]  
        return res
'''