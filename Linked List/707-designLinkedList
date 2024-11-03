# This solves Leetcode problem #707. Design Linked List with a singly linked list
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
        self.size = 0   

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return

        prev = self.head
        for i in range(index):
            prev = prev.next
        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1       

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.head
        for i in range(index):
            prev = prev.next
        prev.next = prev.next.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1

# Time complexity: O(N) for get, addAtHead, addAtTail, addAtIndex, deleteAtIndex
# Space complexity: O(1) for all operations

