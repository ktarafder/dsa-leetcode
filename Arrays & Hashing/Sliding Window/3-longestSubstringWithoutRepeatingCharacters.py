class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

# Time complexity: O(n) b/c we're iterating through the entire string
# Space complexity: O(n) b/c worse case every single character is unique and will be added to the set
# This problem utilizies the sliding window technique where you have two pointers
    # In this example, we're using a variable length sliding window