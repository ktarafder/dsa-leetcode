'''
Write a function solve that finds the longest common prefix among an array of strings.

Example:
Input: ["flower","flow","flight"]
Output: "fl" 
'''

# O(s) time complexity and O(m) space complexity
def solve(strs):
  if len(strs) == 1:
    return strs[0]
  f1rst = strs[0]
  res_len, res = 201, ""
  for i in range(1, len(strs)):
    j, ct, curr = 0, 0, []
    for char in strs[i]:
      if j < len(f1rst) and char == f1rst[j]:
        j += 1
        ct += 1
        curr.append(char)
      else:
        break
    prev = res_len
    res_len = min(res_len, ct)
    if prev > res_len:
      res = "".join(curr)
  return res

print(solve(["flower","flow","flight"]))