'''
Write a function solve that checks if an integer is an Armstrong number (a.k.a Narcissistic number). 

An Armstrong number is a number that is equal to the sum of its digits, each raised to the power of the number of digits

Example:
Input: 153
Output: True
Explanation: 1^3 + 5^3 + 3^3 = 153
'''

'''
Almost one shotted i just forgot to save the value num to another variable since I alter the num val in the while loop
the algo is a log(n) time complexity since we are dividing by 10 each time
the space complexity is log(n) since we are storing the digits in a list
'''

def solve(num):
  n = len(str(num))
  original_num = num
  curSum = 0
  while num != 0:
    last_digit = num % 10
    curSum += last_digit ** n
    num //= 10
  return original_num == curSum

print(solve(153))

# this ugly string based approach exists as well
def solve(num):
    s = str(num)
    p = len(s)
    total = sum(int(d)**p for d in s)
    return total == num

print(solve(153))
