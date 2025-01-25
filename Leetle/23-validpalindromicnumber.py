'''
Write a function solve that checks whether an integer is a palindrome without converting it to a string. 
'''


def solve(num):
  if num < 0: # negative num edge case b/c a negative number cannot be a palindrome 
    return False 
  reversed_num = 0
  orginal_num = num
  while num != 0:
    last_digit = num % 10
    reversed_num = reversed_num * 10 + last_digit
    num //= 10
  print(reversed_num)
  return orginal_num == reversed_num

print(solve(121))

# Simplified 
def solve(num):
    if num < 0: return False
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev == original
print(solve(121))

'''
Dry run for the test case above 
rev, num = 0, 121

ld = 121 % 10 = 1
rev = 0 * 10 + 1 = 1
num = num // 10 = 121 // 10 = 12

ld = 12 % 10 = 2
rev = 1 * 10 + 2 = 12
num = num // 10 = 12 // 10 = 1

ld = 1 % 10 = 1
rev = 12 * 10 + 1 = 121
num = num // 10 = 1 // 10 = 0
'''