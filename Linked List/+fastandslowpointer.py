class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

'''
Example 1: Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.
'''

def get_mid(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

one = ListNode(1); one.next = ListNode(2); one.next.next = ListNode(3); one.next.next.next = ListNode(4); one.next.next.next.next = ListNode(5)
print(get_mid(one))

'''
Given the head of a linked list, determine if the linked list has a cycle.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointe
'''

def check_cycle(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == head:
            return True
    return False

print(check_cycle(one))
one = ListNode(1); one.next = ListNode(2); one.next.next = ListNode(3); one.next.next.next = ListNode(4); one.next.next.next.next = ListNode(5); one.next.next.next.next.next = one
print(check_cycle(one))

'''
Example 3: Given the head of a linked list and an integer k, return the kth node from the end.

For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.
'''

def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow

one = ListNode(1); one.next = ListNode(2); one.next.next = ListNode(3); one.next.next.next = ListNode(4); one.next.next.next.next = ListNode(5)
print(find_node(one, 2).val)