# Brute force O(n^2) 
def twosum(nums, target):
    for i in range(len(nums)):
        diff = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == diff:
                return [i, j]

print(twosum([5,2,7,10,3,9], 8))

# Hashmap O(n)
def bettertwosum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

print(bettertwosum([5,2,7,10,3,9], 8))