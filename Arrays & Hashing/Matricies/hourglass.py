'''
Given a 6x6 2D array find all hourglass sums in the array
An hourglass falls within this pattern:
a b c
  d
e f g
'''

def hourglassSum(arr):
    res = float('-inf')
    for i in range(1, 5):  
        for j in range(1, 5):  
            curr = (
                arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +  # Top row
                arr[i][j] +  # Middle
                arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]  # Bottom row
            )
            res = max(res, curr)
    return res