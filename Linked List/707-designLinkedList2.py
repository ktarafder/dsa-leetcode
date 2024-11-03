# # This solves Leetcode problem #707. Design Linked List with a doubly linked list
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.left = ListNode() # dummy left node
        self.right = ListNode() # dummy right node
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next 

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next 

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = ListNode(val), curr, curr.prev
            prev.next, next.prev = node, node
            node.prev, node.next = prev, next 

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            next, prev = curr.next, curr.prev
            next.prev = prev
            prev.next = next

# Time complexity: O(N) for all functions
# Space complexity: O(1) for all functions