'''
Problem:

You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
'''

# This algorithm is O(n) [amortized constant work inside of the for loop] time and O(k) space as the algorithm deletes elements from the hashmap once it grows beyond k
def distinct(s, k):
    # sliding window with hashmap
    counts = {} # char : frequency
    l = 0
    res = 0
    for r in range(len(s)): 
        counts[s[r]] = 1 + counts.get(s[r], 0) # constraint metric freq of distinct chararacters, numeric restriction is k
        while len(counts) > k: 
            counts[s[l]] -= 1
            if counts[s[l]] == 0:
                del counts[s[l]]
            l += 1
        res = max(res, r-l+1)
    return res

print(distinct("eceba", 2)) # 3

'''
Another approach to handling when we come across a character that isn't in our dictionary is to use an int default dictionary
'''

from collections import defaultdict

def distinctdd(s, k):
    # sliding window with hashmap
    counts = defaultdict(int) # char : frequency
    l = 0
    res = 0
    for r in range(len(s)): 
        counts[s[r]] += 1 # constraint metric freq of distinct chararacters, numeric restriction is k
        while len(counts) > k: 
            counts[s[l]] -= 1
            if counts[s[l]] == 0:
                del counts[s[l]]
            l += 1
        res = max(res, r-l+1)
    return res

print(distinctdd("eceba", 2)) # 3