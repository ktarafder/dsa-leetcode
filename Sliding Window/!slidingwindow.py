def solution(nums, k):
    l, curr, res = 0, 0, 0
    for r in range(len(nums)):
        curr += nums[r] # constraint metric is sum
        while curr > k: # numeric restriction is k
            curr -= nums[l]
            l += 1
        res = max(res, r - l + 1)
    return res

#print(solution([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))

def sol(s):
    l, curr, res = 0, 0, 0
    for r in range(len(s)):
        if s[r] == '0':
            curr += 1
        while curr > 1:
            if s[l] == '0':
                curr -= 1
            l += 1   
        res = max(res, r - l + 1)
    return res

#print(sol('1101100111'))

'''
Sliding Window:
Constraint metric [attribute of window like sum] & numeric restriction 
constraint metric conforms to numeric restriction
Slide window to the right by adding element to window arr[right]
if window invalidates numeric restriction then we decrease window size until it is valid again by removing arr[left]
calculate window size with r - l + 1 
'''

# Fixed size sliding window 
def sub(nums, k):
    curr, res = 0,0
    for i in range(k): # sum of the first window
        curr += nums[i]
    res = curr
    for i in range(k, len(nums)): # we can start from second window all we need to do is remove left pointer val and add right pointer val concurrently done in line below
        curr += nums[i] - nums[i-k] # our right value "pointer" is nums[i] while the left value "pointer" is nums[i-k]
        res = max(res, curr)
    return res

# print(sub([3, -1, 4, 12, -8, 5, 6], 4))

# constraint is the mean of window (max avg val)
# fixed size window
def fix(nums, k):
    curr, res = 0, 0
    for i in range(k):
        curr += nums[i]
    res = curr / k
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]
        res = max(res, curr / k)
    return res

# constraint metric of freq 0
# numeric restriction of <= 2

def dyn(nums, k):
    l, curr, res = 0, 0, 0
    for r in range(len(nums)):
        if nums[r] == 0:
            curr += 1
        while curr > k:
            if nums[l] == 0:
                curr -= 1
            l += 1
        res = max(res, r-l+1)
    return res

print(dyn([1,1,1,0,0,0,1,1,1,1,0], 2))
