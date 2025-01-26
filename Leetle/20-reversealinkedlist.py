'''
Write a function that, given the head of a singly linked list, reverses the list. Return the root node of the reversed list.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
'''
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
       
def solve(head):
    curr = head
    prev = None
    while curr:
        nextNode = curr.next
        curr.next = prev

        prev = curr
        curr = nextNode

    return prev

LL = ListNode(1); LL.next = ListNode(2); LL.next.next = ListNode(3); LL.next.next.next = ListNode(4); LL.next.next.next.next = ListNode(5)
reversed_head = solve(LL)

curr = reversed_head
while curr:
    print(curr.val)
    curr = curr.next
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