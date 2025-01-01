def summation(n: int) -> int:
    for i in range(n):
        n += i
    return n

print(summation(8)) 

def summation_formula(n: int) -> int:
    return n * (n+1) / 2

print(summation(8))

'''
We can see that the first function is O(n) time while the second one takes O(1) time
Knowing about the summation formula allows us to reduce our time complexity
'''