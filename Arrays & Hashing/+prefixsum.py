import unittest

def answer_queries(nums, queries, limit):

    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])


    # Another way of constructing the prefix sum arr 
    '''
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    What this method allows us to do is it prevents us from worrying about the edge case where i = 0 with the previous code construction
    That's because this code produces a prefix sum array that represents the sum of elements up to, but not including, the current index
    i + 1 gives us the prefix sum of the previous n elements including i where as just i gives us the sum of the previous i-1 + i-2 + ... + 0 elements 
    So in the code below we can simplify our calculation to prefix[y+1] - prefix[x] 
    '''
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x] # 12 - 1 + 1 = 12, 21 - 10 + 3 = 14 --> adding nums[x] lets us go back the prefix[x - 1], this accounts for the edge case of i = 0 where if we try accessing prefix[x-1] we get an out of bounds error.
                                               # Basically we're adding the value of x back in b/c if we subtract prefix[x] from prefix[y] it's not inclusive of value x
        ans.append(curr < limit)

    return ans

# thanks to prefic sum the algorithm goes from a O(n*m) tc in brute force to a O(n+m) tc
# prefix sum uses O(n) memory to construct the prefix sum array

# mayb writing tests will actually land me a job
class TestAnswerQueries(unittest.TestCase):
    def test_answer_queries(self):             # 0  1   2   3   4   5
        nums = [1, 6, 3, 2, 7, 2] # prefix arr: [1, 7, 10, 12, 19, 21]
        queries = [[0, 3], [2, 5], [2, 4]]
        limit = 13
        expected_output = [True, False, True]
        self.assertEqual(answer_queries(nums, queries, limit), expected_output)

if __name__ == '__main__':
    unittest.main()