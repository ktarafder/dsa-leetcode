'''
Write a function solve that finds the kth largest element in an unsorted array.

Example:
Input: [3,2,1,5,6,4], 2
Output: 5 
'''

# TODO: Understand the quickselect 

# You learn something new everyday and today I learned that you can pass in a reverse argument to both 
# the Python sorted() function and .sort() method to easily reverse sort iterables or arrays

# Sorting approach
# This has O(nlogn) time complexity and O(n) space complexity since a new array is being created
def solve(nums, k):
    return sorted(nums, reverse=True)[k-1]

# More efficient sorting approach since it sorts in place so no additional memory is used
def solve(nums, k):
  nums.sort(reverse=True) # cant directly do [k-1] like previous example because this isnt subscriptable since it doesnt return a new array, it modifies the original array in place
  return nums[k-1]

# Heap based approach using min heap
# This has O(nlogk) time complexity and O(k) space complexity
def solve(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]

# Quickselect using Lomuto's partitioning 
import random

def quickselect_largest(nums, k):
    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # Move pivot to end
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1

        nums[store_index], nums[right] = nums[right], nums[store_index]  # Move pivot to final place
        return store_index

    def select(left, right, k_smallest):
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    n = len(nums)
    return select(0, n - 1, n - k)  # Convert k-th largest to (n-k)-th smallest

print(quickselect_largest([3,2,1,5,6,4], 2))