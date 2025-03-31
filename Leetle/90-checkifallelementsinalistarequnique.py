'''
Write a function solve that checks if all elements in a list are unique (no duplicates).

Example:
Input: [1, 2, 3, 4]
Output: True 
'''

def solve(arr):
  hashset = set()
  for i in range(len(arr)):
    if arr[i] in hashset:
      return False
    hashset.add(arr[i])
  return True

print(solve([1,2,3,4]))
print(solve([1,2,1,3]))

# Cool python one liner solution to this
def oneliner(arr):
  return len(arr) == len(set(arr))

print(oneliner([1,2,3,4]))
print(oneliner([1,2,1,3]))
