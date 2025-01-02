# 01/01/2025
'''
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
'''

'''
So for this problem, right away I had the idea to use a prefix sum. My problem was I was so locked into a prefix sum array
In this problem we can use a prefix sum integer to first add up the sum of the 1s
Basically initially we treat the entire string as the right substring, therefore the current value or score of the substring is all the 1s added up
Now that we have a score for the right substring we can continuously increment through the string where each element encountered is removed from the right substring and added to the left substring
We can keep track of the sum on the left by having a variable for zero sum that increments when we encounter a zero on the left
Now here s[i] == 1 or s[i] == 0 if the value is 1 then we decrement our sum of ones value b/c we have lost a 1 counting toward score otherwise we increment our sum of zeroes value
We can take the max each time to measure max score against current res versus zeroes + ones then return res
'''

def solution(s):
    ones, zeroes, res = 0, 0, 0
    for i in range(len(s)):
        ones += int(s[i])
    
    for i in range(len(s)-1): # -1 b/c we cant have a partition at the very end
        if s[i] == "1":
            ones -= 1
        else:
            zeroes += 1
        res = max(res, ones+zeroes)
    
    return res

print(solution("011101")) # 5
print(solution("00")) # 1

# brute force
def brute(s):
    if s == "00":
        return 1
    
    res = 0
    for i in range(len(s)):
        curr = 0
        for j in range(i+1):
            if s[j] == "0":
                curr += 1
        
        for j in range(i+1, len(s)):
            if s[j] == "1":
                curr += 1
        
        res = max(res, curr)
    
    return res

print(brute("011101")) # 5
print(brute("00")) # 1 edge case