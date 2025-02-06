'''
Write a function solve that returns the middle node of a singly linked list. If two middles, return the second one.

Example:
Input: [1,2,3,4,5]
Output: 3 
'''

def solve(head):
    slow = head
    fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow