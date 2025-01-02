def sol(matches: List[int]) -> List[List[int]]:
    # hashmap player: # losses 
    counts = defaultdict(int)
    for winner, loser in matches:
        counts[winner] += 0
        counts[loser] += 1

    undefeated, one_loss = [], []
    for player in counts:
        if counts[player] == 0:
            undefeated.append(player)
        elif counts[player] == 1:
            one_loss.append(player)
    return [sorted(undefeated), sorted(one_loss)]

# time complexity O(n + mlogm) space complexity O(m) n is the number of matches and m is the number of unique players
print(sol([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

'''
Problem 1189. Maximum Number of Balloons
'''

from collections import defaultdict

def maxBalloons(text: str) -> int:
    # hashmap of char frequency 
    counts = defaultdict(int)
    for c in text:
        counts[c] += 1
    
    return min(
        counts['b'],
        counts['a'],
        counts['l'] // 2,
        counts['o'] // 2,
        counts['n']
    )

print(maxBalloons('loonbalxballpoon'))

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = [0] * 26
        for c in text:
            freq[ord(c) - ord('a')] += 1
        
        return min( freq[1],        # b
                    freq[0],        # a
                    freq[11] // 2,  # l
                    freq[13],       # n
                    freq[14] // 2)  # o

'''
Problem 2287. Rearrange Characters to Make Target String
Slighlty more diffcult version of previous problem
Both of the below solutions have a time complexity of O(n + m) n is the length of string and m is the length of target
Both of a space complexity of O(1) b/c we're bounded by a size of 26 (lowercase english letters)
'''

# Hashing approach
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # construct freq hashmap for string
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        # construct freq hashmap for target 
        target_counts = defaultdict(int)
        for c in target:
            target_counts[c] += 1
        
        
        return min(counts.get(c, 0) // target_counts[c] for c in target_counts)

# Array approach 
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq_s = [0] * 26
        freq_t = [0] * 26

        for c in s:
            freq_s[ord(c) - ord('a')] += 1
        
        for c in target:
            freq_t[ord(c) - ord('a')] += 1
        
        res = float('inf')
        for c in range(26):
            if freq_t[c] > 0:
                res = min(res, freq_s[c] // freq_t[c])
        
        return res

'''
1133. Largest Unique Number

Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.
'''
from typing import List
from collections import defaultdict

def solution(nums: List[int]):
    # frequency of each integer
    # max(freq if freq[int] == 1)
    # if not return -1
    freq = defaultdict(int)
    for n in nums:
        freq[n] += 1
    res = [num for num in freq if freq[num] == 1]
    if not res: # if res is empty then there is no number with frequency of 1
        return -1
    return max(res)

print(solution([5,7,3,9,4,9,8,3,1]))
print(solution([9,9,8,8]))

'''
525. Contiguous Array - Meta Question

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
'''

def cont_sub(nums: List[int]):
    nums = [-1 if num == 0 else 1 for num in nums]
    sum_map = {0:-1}
    curr, res = 0,0

    for i, n in enumerate(nums):
        curr += n
        if curr in sum_map:
            res = max(res, i - sum_map[curr])
        else:
            sum_map[curr] = i
    return res

print(cont_sub([0,1,0]))

from collections import Counter

def canConstruct(note, mag):
    freqn, freqm, res = Counter(note), Counter(mag), 0
    for char in freqm:
        if char in freqn:
            if freqn[char] > freqm[char]:
                return False 
            res += freqn[char]
    return res == len(note)

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))