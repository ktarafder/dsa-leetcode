import unittest

# time and space complexity of O(n)
def waystoSplit(nums):
    # construct prefix sum
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    # we can have n-1 arr splits where n is the length of the arr
    res = 0
    for i in range(len(nums)-1): # cannot split at last index so we stop before we reach last index
        l, r = prefix[i], prefix[-1] - prefix[i]
        if l >= r:
            res += 1
    return res

print(waystoSplit([1, 2, 3, 4, 5]))

# turns out we can do this without a prefix array to reduce space complexity down to O(1)
# integer prefix sum
def waystoSplit2(nums):
    l, res = 0, 0
    total = sum(nums)
    for i in range(len(nums)-1):
        l += nums[i]
        r = total - l
        if l >= r:
            res += 1
    return res


class TestWaystoSplit(unittest.TestCase):
    def test_waystoSplit_case1(self):
        nums = [10, 4, -8, 7]
        expected_output = 2
        self.assertEqual(waystoSplit(nums), expected_output)
        self.assertEqual(waystoSplit2(nums), expected_output)

    def test_waystoSplit_case2(self):
        nums = [2, 3, 1, 0]
        expected_output = 2
        self.assertEqual(waystoSplit(nums), expected_output)
        self.assertEqual(waystoSplit2(nums), expected_output)

    def test_waystoSplit_case3(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = 1
        self.assertEqual(waystoSplit(nums), expected_output)
        self.assertEqual(waystoSplit2(nums), expected_output)

    def test_waystoSplit_case4(self):
        nums = [5, -2, 3, 1, 2]
        expected_output = 3
        self.assertEqual(waystoSplit(nums), expected_output)
        self.assertEqual(waystoSplit2(nums), expected_output)

if __name__ == '__main__':
    unittest.main()