def solution(N):
    binary_str = bin(N)[2:] # O(log(N)) for both time and space complexity

    max_gap = 0  
    current_gap = 0  

    for bit in binary_str: # O(log(N))
        if bit == '1':
            max_gap = max(max_gap, current_gap)
            current_gap = 0 
        else:
            current_gap += 1

    return max_gap

# Test cases
N = 1041
print(solution(N)) # Expected output: 5

N = 32
print(solution(N)) # Expected output: 0

# Time complexity: O(log(N)) 
# Space complexity: O(log(N))
# The process of converting an integer to binary is O(log(N)) b/c we're dividing by 2 each time
# The for loop is O(log(N)) b/c we're iterating through the binary string
# The space complexity is also O(log(N)) b/c we're storing the binary string in memory, and log(N) is the length of the binary representation of N
# Other ways of solving this problem include string parsing or bit manipulation

# String parsing approach
'''
def solution(N):
    # Convert the number to binary and strip the '0b' prefix
    binary_rep = bin(N)[2:]

    # Split the binary representation by '1' to extract potential gaps
    gaps = binary_rep.split('1')

    # If the binary number ends with zeros, the last split part won't be a valid gap
    if binary_rep.endswith('0'):
        gaps.pop()  # Remove the trailing zeros

    # Find the length of the longest gap, or return 0 if no gaps exist
    return max((len(gap) for gap in gaps), default=0)

    Example Runs:

    Input: N = 1041
    Binary: '10000010001'
    Gaps: ['', '00000', '000', '']
    Longest Gap: 5
    Output: 5

    Input: N = 32
    Binary: '100000'
    Gaps: ['', '00000'] # We will pop the last element from the gaps list since it's a trailing gap
    Longest Gap: 0
    Output: 0
'''

