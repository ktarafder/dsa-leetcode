from typing import List
# This is a sliding window problem bro 
'''
Circular array trick:
Use the modulo operator to wrap around the list i.e. make it circular so we don't get an index out of bounds error
'''
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        l = 0
        curr_sum = 0

        if k == 0:
            return res
        
        for r in range(N + abs(k)):
            curr_sum += code[r % N]

            if r - l + 1 > abs(k):
                curr_sum -= code[l % N]
                l = (l + 1) % N
            
            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % N] = curr_sum
                elif k < 0:
                    res[(r + 1) % N] = curr_sum
        
        return res

# Time complexity: O(n) where n is the length of the code list
# Space complexity: O(n) where n is the length of the code list

# Test cases
# Example 1
sol = Solution()
print(sol.decrypt([5,7,1,4], 3)) # Expected: [12,10,16,13]

# Example 2
print(sol.decrypt([1,2,3,4], 0)) # Expected: [0,0,0,0]

# Example 3
print(sol.decrypt([2,4,9,3], -2)) # Expected: [12,5,6,13]

'''
Brute force solution to defusing the bomb
The trick is to use the modulo operator to wrap around the list i.e. make it circular so we don't get an index out of bounds error
'''
'''
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        res = [0] * N

        if k == 0:
            return res
        
        for i in range(N):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                    res[i] += code[j % N]
            elif k < 0:
                for j in range(i - 1, i - 1 - abs(k), -1):
                    res[i] += code[j % N]
        
        return res

# Time complexity: O(n * k) where n is the length of the code list
# Space complexity: O(n) where n is the length of the code list

# Test cases
# Example 1
sol = Solution()
print(sol.decrypt([5,7,1,4], 3)) # Expected: [12,10,16,13]

# Example 2
print(sol.decrypt([1,2,3,4], 0)) # Expected: [0,0,0,0]

# Example 3
print(sol.decrypt([2,4,9,3], -2)) # Expected: [12,5,6,13]
'''