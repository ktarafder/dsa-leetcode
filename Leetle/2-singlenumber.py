'''
I actually solved this right before midnight and didn't add the problem on here so I forgot the exact wording of the question, but it was smthing like:
Find the number that appears only once in a list where all other numbers appear twice
I think I got it on the third attempt b/c first one I forgot to import Counter second time I was being dumb and forgot Python third time was the fix
'''

from collections import Counter
def solve(nums):
  counts = Counter(nums) # Creating Counter: O(n) where n is the length of nums
  return [i for i in counts if counts[i] == 1][0] # List comprehension is O(n) 

# O(n) memory b/c dictionary can store counts for each unique number
print(solve([4,1,2,1,2])) # 4


def solve(nums):
  counts = Counter(nums)
  for i in counts:
    if counts[i] == 1:
      return i # counts[i] I was doing this and wondering why it wasn't working smh 🤦🏽‍♂️ 

print(solve([4,1,2,1,2])) # 4

# fun one liner math solution but this is still an O(n) time due to the sums and hashset and O(n) space due to the hashset
def solve(nums):
  return 2 * sum(set(nums)) - sum(nums)

print(solve([4,1,2,1,2])) # 4

# XOR-based solution
# I don't even understand how this works but I think it's cool plus it reduces space complexity to O(1)
def solve(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

print(solve([4,1,2,1,2])) # 4

'''
Claude's explanation

The XOR operation (^) has these key properties:

a ^ a = 0 (any number XOR with itself equals 0)
a ^ 0 = a (any number XOR with 0 equals itself)
a ^ b ^ a = b (XOR is associative and the order doesn't matter)

Dry run with [4,1,2,1,2]
result = 0
result ^= 4  # 0 ^ 4 = 4
result ^= 1  # 4 ^ 1 = 5
result ^= 2  # 5 ^ 2 = 7
result ^= 1  # 7 ^ 1 = 6
result ^= 2  # 6 ^ 2 = 4

Because all duplicates will XOR to 0, and 0 XOR with any number gives that number, 
we're left with the single number that appears only once (4 in this case).
'''