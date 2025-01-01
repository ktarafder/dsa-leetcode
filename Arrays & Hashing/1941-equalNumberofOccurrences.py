'''
Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. All characters appear twice. Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
'''

from collections import defaultdict


def sol(s: str):
    # hashmap store frequency of char
    # map[i] != map[i + 1] all the way through we can return False else True 
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    
    freqs = counts.values()
    print(freqs) # dict_values([2,2,2]) we can convert to normal list list(freqs)
    print(set(freqs))
    return len(set(freqs)) == 1

print(sol("abacbc")) # True
print()
print(sol("aaabb")) # False

# One liner solution
from collections import Counter

def sol2(s: str) -> bool:
    return len(set(Counter(s).values())) == 1

print(sol2("abacbc")) # True
print(sol2("aaabb")) # False
