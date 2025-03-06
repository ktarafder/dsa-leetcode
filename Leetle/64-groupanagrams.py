'''
Write a function solve that groups anagrams together.

Example:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]] 
'''

from collections import defaultdict

def solve(strs):
  grams = defaultdict(list)
  for s in strs: # dont do for s in range(len(strs)) my mistake there 
    vals = [0] * 26
    for c in s:
      vals[ord(c) - ord('a')] += 1 # ord('a') == 97
    grams[tuple(vals)].append(s)
  return list(grams.values())

print(solve(["eat","tea","tan","ate","nat","bat"]))