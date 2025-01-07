'''
Write a function solve that determines if two strings are anagrams of each other. An anagram is a word formed by rearranging the letters of another word.

Example:
Input: "listen", "silent"
Output: true 
'''

'''
I have solved this problem too many times 
Counter ftw
'''

from collections import Counter

def solve(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)

print(solve("listen", "silent")) # True

# Checking to see if I can still do this without using Counter or defaultdict
# turns out I can
def solve(s1: str, s2: str) -> bool:
    counts1, counts2 = {}, {}
    for c in s1:
        counts1[c] = 1 + counts1.get(c, 0)
    for c in s2:
        counts2[c] = 1 + counts2.get(c, 0)
    return counts1 == counts2

print(solve("listen", "silent")) # True

# Optimization
'''
add if len(s1) != len(s2): return False 
'''