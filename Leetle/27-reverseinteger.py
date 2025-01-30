'''
Write a function solve that reverses the digits of an integer. If the reversed integer overflows, return 0.

Example:
Input: 123
Output: 321
Assume the input is a 32-bit signed integer, so the reversed integer must be within the range [-2^31, 2^31-1]. 
'''

'''
Solving leetle #23 helped a lot with this one. I instantly knew the reversing logic, just needed to handle
negative numbers and 
'''

def solve(n):
  neg = False
  if n < 0:
    neg = True
    n = abs(n)
  if n > 2 ** 30:
    return 0
  rev = 0
  while n != 0:
    last_digit = n % 10
    rev = rev * 10 + last_digit
    n //= 10
  return -rev if neg else rev

print(solve(123))

# Simplified version of my code
def solve(n):
    sign = 1 if n>=0 else -1
    n = abs(n)
    rev = 0
    while n:
        rev = rev*10 + n%10
        n //= 10
    rev *= sign
    return rev if -2**31 <= rev <= 2**31-1 else 0