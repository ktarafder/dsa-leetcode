'''
Write a function that, given the head of a singly linked list, reverses the list. Return the root node of the reversed list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
'''

def solve(head):
    curr = head
    prev = None
    while curr:
        nextNode = curr.next
        curr.next = prev

        prev = curr
        curr = nextNode

    return prev

'''
prev = None
curr = head = 1
1 -> 2 -> 3 -> 4 -> 5

next = curr.next = 2
curr.next = prev = None | 1 -> None 
prev = curr = 1
curr = next = 2

next = curr.next = 3
curr.next = prev = 1 | 2 -> 1
prev = curr = 2
curr= next = 3
'''