import unittest

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x] # 12 - 1 + 1 = 12, 21 - 10 + 3 = 14 --> adding nums[x] lets us go back the prefix[x - 1], this accounts for the edge case of i = 0 where if we try accessing prefix[x-1] we get an out of bounds error.
                                               # Instead if i = 0 we're just cancelling out the value with itself 
        ans.append(curr < limit)

    return ans

# thanks to prefic sum the algorithm goes from a O(n*m) tc in brute force to a O(n+m) tc
# prefix sum uses O(n) memory to construct the prefix sum array

# mayb writing tests will actually land me a job
class TestAnswerQueries(unittest.TestCase):
    def test_answer_queries(self):
        nums = [1, 6, 3, 2, 7, 2]
        queries = [[0, 3], [2, 5], [2, 4]]
        limit = 13
        expected_output = [True, False, True]
        self.assertEqual(answer_queries(nums, queries, limit), expected_output)

if __name__ == '__main__':
    unittest.main()