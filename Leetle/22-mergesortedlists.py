'''
Write a function solve that merges two sorted lists into one sorted list. 
'''
'''
I love my one liners and realized instantly this could be solved with a one liner, took some time though b/c I forgot that you could add lists together 
In this case, I was aware the one liner is inefficient compared to the two pointer based solution below the one liner solution 
One liner time complexity using sorting: O((n+m)log(n+m)) while two pointer time complexity: O(n+m)
Space complexity is the same for both O(n+m)
'''

def solve(list1, list2):
  return sorted(list1 + list2)

def solve(list1, list2):
  l1, l2 = 0, 0
  res = []
  while l1 < len(list1) and l2 < len(list2):
    if list1[l1] < list2[l2]:
      res.append(list1[l1])
      l1 += 1
    else:
      res.append(list2[l2])
      l2 += 1
  res += list1[l1:] + list2[l2:]
  return res