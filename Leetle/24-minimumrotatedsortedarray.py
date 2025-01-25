'''
Write a function solve that finds the minimum element in a rotated sorted array. 

Example:
Input: [3,4,5,1,2]
Output: 1 
'''

'''
I will admit I did cheese this problem by just doing return min(nums)
I did recognize though the right way to do this problem is to use binary search for log(n) time complexity 
'''

def solve(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l+r)//2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid # the nums[mid] value could be the minimum element which is why we set the right pointer directly equal to mid 
    return nums[l] # we could also return nums[r] it doesn't matter since both pointers will be pointing to the same index 

print(solve([3,4,5,1,2]))