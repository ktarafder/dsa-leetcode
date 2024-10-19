# I wrote this all in vim with no syntax highlighting
# Chat am I cracked now?
def binary_search(target, arr):
	l, r = 0, len(arr) - 1
	while l <= r:
		m = (l + r) // 2
		if arr[m] == target:
			return m
		elif arr[m] > target:
			r = m - 1
		else:
			l = m + 1
	return -1


target = 8
arr = [1, 2, 3, 4, 5, 8, 10]
print(binary_search(target, arr))
