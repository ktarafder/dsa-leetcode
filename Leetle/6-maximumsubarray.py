'''
Write a function solve that finds the nonempty contiguous subarray with the largest sum in a list.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6 
'''

'''
Yikes this problem took 29:30 and in the end I had to go with a brute force approach and got it on the very last attempt.
Initially I read the problem and I saw subarray and immediately my brain leaped to sliding window, but a sliding window doesn't work here 
So I wasted 5 minutes going down the sliding window approach
Looked at this same problem on leetcode to better understand it and went extensively through the first test case to understand how we arrived at 6 (I should have done this from the beginning)
Once I understood that I realized that there is prlly a dynamic programming approach to this, which when i googled I was right
However I still don't know how the heck to implement dynamic programming, so I realized that imma just have to go down the brute force route 

'''
def solve(nums):
   res = nums[0] # set this to first element, not 0 b/c what if the first element is a negative number and the array contains all negative numbers if we return 0 then our answer is incorrect
   for i in range(len(nums)):
    curr = 0
    curr += nums[i]
    res = max(res, curr) # this allows us to consider if the singular element subarray nums[i] has the maximum sum and also the last element since the inner loop doesn't execute for second last element
    for j in range(i, len(nums) - 1):
      curr += nums[j+1]
      res = max(res, curr) # put this inside the inner loop b/c must consider every contigous subarray not just i till the end (which I was going by putting this after the inner loop)
   return res

print(solve([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(solve([1])) # 1

# After I submitted my solution I realized that there is this cleaner brute force solution
def solve(nums):
   res = nums[0] # set this to first element, not 0 b/c what if the first element is a negative number and the array contains all negative numbers if we return 0 then our answer is incorrect
   for i in range(len(nums)):
    curr = 0
    for j in range(i, len(nums)):
      curr += nums[j]
      res = max(res, curr) # put this inside the inner loop b/c must consider every contigous subarray not just i till the end (which I was going by putting this after the inner loop)
   return res

print(solve([-2,1,-3,4,-1,2,1,-5,4]))
print(solve([1]))

# Kadane's Algorithm
# Runs in O(n) time compared to the O(n^2) brute force solution
def solve(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(solve([-2,1,-3,4,-1,2,1,-5,4]))
print(solve([1]))