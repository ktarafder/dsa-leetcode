# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        dummyNode = ListNode()
        tail = dummyNode

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummyNode.next
    
        # Print the linked list
        '''
        curr = dummyNode.next
        while curr:
            print(curr.val, end=" -> ") 
            curr = curr.next
        '''

# Time complexity: O(n + m)
# Space complexity: O(1)

# Test cases
# Test 1
l1 = ListNode(1, ListNode(2, ListNode(4))) # 1 -> 2 -> 4
l2 = ListNode(1, ListNode(3, ListNode(4))) # 1 -> 3 -> 4
print(Solution().mergeTwoLists(l1, l2))  # 1