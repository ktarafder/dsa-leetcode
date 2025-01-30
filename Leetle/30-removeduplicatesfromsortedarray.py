'''
Write a function solve that removes duplicates from a sorted array in-place, and return the new length.

Example:
Input: [1,1,2]
Output: 2 
'''

'''
I solved this problem NOT in the way it was meant to be solved, I knew there was a trick to it because it's sorted but I was lazy to 
think through all the different strategies or pattern I could apply to this problem
In this case a two pointers approach gives you a more efficient space complexity, time complexity doesn't change though between the two
'''

def solve(nums):
    hashset = set()
    for i in range(len(nums)):
        hashset.add(nums[i])
    return len(hashset)

print(solve([1,1,2]))

# More efficient two pointer approach
def solve(nums):
    if len(nums) == 0:
        return 0
    l = 1
    for r in range(len(nums)):
        if nums[r] != nums[r-1]:
            l += 1
            nums[l] = nums[r]
    return l

print(solve([1,1,2]))