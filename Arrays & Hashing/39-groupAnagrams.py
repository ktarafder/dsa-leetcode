from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # defaultdict allows for simulatenous key creation and value assignment b/c it assigns an empty list to the key and then will append the value to the list
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # Tuple b/c lists are mutable so they can't be keys in a dict
        return list(res.values())
    
sol = Solution()
# Test cases
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["bat"],["nat","tan"],["ate","eat","tea"]]

# 7:30 - should have mentioned edge cases like empty list