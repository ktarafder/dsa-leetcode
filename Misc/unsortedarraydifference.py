def solve(arr1, arr2):
   arr1 = sorted(arr1)
   arr2 = sorted(arr2)
   ptr1,ptr2 = 0,0
   res = []
   while ptr1 < len(arr1) and ptr2 < len(arr2):
      difference = arr1[ptr1] - arr2[ptr2]
      res.append(difference)
      ptr1 += 1
      ptr2 += 1
   res += arr1[ptr1:] + arr2[ptr2:]
   return res

print(solve([3,2], [1,2,3]))