'''
Write a function solve that takes a number n and returns a list of numbers from 1 to n. If the number is divisible by 3, replace it with 'Fizz'. If the number is divisible by 5, replace it with 'Buzz'. If the number is divisible by both 3 and 5, replace it with 'FizzBuzz'.

Example:
Input: 15
Output: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'] 
'''

'''
4:58
❌❌❌❌❌❌ --> I did not read the question properly 😭 thought it was normal boolean return at first
✅✅✅✅✅✅
'''

# flexin my one liner 💪🏽
def solve(n):
  return ["Fizz" * (i%3==0) + "Buzz" * (i%5==0) or i for i in range(1,n+1)]