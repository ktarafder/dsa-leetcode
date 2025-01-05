'''
Resources:
https://www.youtube.com/watch?v=96RG7EBF8LI&t=531s&ab_channel=TLEEliminators-byPriyansh

Difference array utilizes the prefix sum concept. Let's say we want to populate a subarray from index i to j (inclusive) with a particular number.
In this problem, we're given an array and a matrix of queries where queries[0] = i, queries[1] = j, and queries[2] = num
Brute force approach is to replace each index in given array from i to j with the number
The issue with this is that the time complexity is O(q*n) where q is the number of queries and n is the length of the array
We can simplify this down to O(q+n) by using a difference array 
We know that in a prefix sum to find the value of a subarray we can perform j - (i-1)
array: [1,2,3,4,5]
prefix: [1,3,6,10,15]
If want to find sum of subarray (1,3) we can do prefix[3] - prefix[0] = 10-1 = 9
Similarly with a difference array approach if we have want to populate from i to j a number 
that number is basically a prefix sum from i to j b/c let's say we query [1,3,3] in the array [0,0,0,0,0]
then we get --> [0,3,3,3,0] if we just say that arr[start] = 3 to get [0,3,0,0,0]
if we set a curr variable to 3 we can iterate through, adding that value to each index
The problem is: how can we tell our prefix sum to stop?
The solution to this is we take the negative of num and place it at j+1 aka end+1
This results in our 3 propagating in the prefix sum until it hits end+1 b/c it will cancel out to 0 i.e. 3 - 3 = 0 the rest of the way
Now you may notice an issue in this: what if our end value is set to the last index position? If we try putting the negative num at j+1 we will get an out of bounds error
The solution this is to intialize our difference array with n+1 values
We can do something like difference_arr = [0] * (n+1) where n is the length of the array or string we're looking at so we don't go out of bounds 
Now we will ignore the last value in our difference array, it doesn't matter, so when we iterate through to calculate the prefix sum we'll just iterate n values
'''

def solve(arr, queries):
    n = len(arr)
    delta = [0] * (n+1)

    for start,stop,num in queries:
        delta[start] += num
        delta[stop+1] -= num
    
    curr = 0
    res = []
    for i in range(n):
        curr += delta[i]
        res.append(curr + arr[i])
    
    return res

print(solve([0,0,0,0,0], [[1,2,3],[1,3,1]])) # [0,3,3,0,0] # [0,4,4,1,0]  
                                             # [0,3,3,0,0] # [0,4,4,1,0]  

print(solve([1,1,1,1,1], [[1,2,3],[1,3,1]])) # [0,3,3,0,0] # [0,4,4,1,0]  
                                             # [1,4,4,1,1] # [1,5,5,2,1]

def solve(arr, queries):
    n = len(arr)
    delta = [0] * (n+1)

    for start,stop,num in queries:
        delta[start] ^= num
        delta [stop+1] ^= num
    
    curr = 0
    res = []
    for i in range(n):
        curr ^= delta[i]
        res.append(curr)
    
    return res

# print(solve([0,0,0,0,0], [[1,2,3],[1,3,1]]))