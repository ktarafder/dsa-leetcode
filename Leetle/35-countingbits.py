'''
Write a function solve that returns an array of the number of 1-bits (Hamming weight) for each number from 0 to n. 
'''

# My solution O(nlogn) tc and O(n) sc
def solve(n):
  res = []
  for i in range(n+1):
    x = bin(i)[2:]
    count = 0
    for bit in x:
      if bit == '1':
        count += 1
    res.append(count)
  return res

print(solve(2))

# More efficient solution with O(n) tc and O(n) sc
    # Utilizes bitwise right shift operator (>>) and logical and (&)
def solve(n):
    res = [0]*(n+1)
    for i in range(1, n+1):
        # dp use precomputed value right shift
        res[i] = res[i>>1] + (i & 1) # all odd numbers lsb is 1 while even is 0 so i & 1 = 0 for all even and i & 1 = 1 for all odd
    return res

print(solve(3))

'''
res[0] will always equal 0
1 -> 01 -> 00 = 0 -> res[0] = 0 -> 0 + 01 & 01 = 0 + 1 = 1
2 -> 10 -> 01 = 1 -> res[1] = 1 -> 1 + 10 & 01 = 1 + 0 = 1
3 -> 11 -> 01 = 1 -> res[1] = 1 -> 1 + 11 & 01 = 1 + 1 = 2
'''