'''
Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
'''

from collections import defaultdict

def sol(nums):
    counts = defaultdict(int)
    # Cost O(n * m) to iterate through all the elements to populate our hashmap
    for arr in nums:
        for val in arr:
            counts[val] += 1
    
    res = [] # can have at most m elements
    n = len(nums)
    # if all elements are unique this loop costs O(n * m)
    for k in counts:
        if counts[k] == n:
            res.append(k)
    
    return sorted(res) # since res has at most m elements worst case sort is O(mlogm)

# Final time complexity: O(m * (n + logm)) = O(n*m + mlogm)
# space complexity: O(n * m) if every element in the input is unique
print(sol([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]])) # [3,4]

