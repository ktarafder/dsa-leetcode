'''
Write a function solve that counts the number of prime numbers less than n. 
'''

'''
I'm getting better at getting sieve's in one go
'''

from math import sqrt

def solve(n):
  if n < 3:
    return 0
  primes = [True] * (n+1)
  primes[0] = primes[1] = False
  for i in range(2, int(sqrt(n) + 1)):
    if primes[i]:
      for j in range(i*i, n+1, i):
        primes[j] = False
  ct = 0
  for i in range(len(primes)):
    if primes[i] == True:
      ct += 1
  return ct

print(solve(30))

# Simplified version for that last loop didn't know you could sum up booleans but ig its a matter of 0s and 1s 
def solve(n):
  if n < 3:
    return 0
  primes = [True] * (n+1)
  primes[0] = primes[1] = False
  for i in range(2, int(sqrt(n) + 1)):
    if primes[i]:
      for j in range(i*i, n+1, i):
        primes[j] = False
  return sum(primes)

print(solve(30))

def solve(n):
  if n < 3: return 0
  sieve = [True] * n
  sieve[0] = sieve[1] = False 
  p = 2
  while p * p < n:
    if sieve[p]:
      for i in range(p*p, n, p): # initial calc of starting value then increments by p each time until n
        sieve[i] = False
    p += 1
  return sum(sieve)

print(solve(30))
