class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Traversing the linked list
    def print_LL(self):
        if not self.head:
            print("Linked List is empty")
        else:
            curr = self.head
            while curr:
                print(curr.value, end=" -> ")
                curr = curr.next

    # Adding a node at the beginning of the linked list
    def add_begin(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    # Adding a node at the end of the linked list
    def add_end(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    # Adding a node between a linked list, after a node
    def add_after(self, value, target):
        curr = self.head
        while curr and curr.value != target:
            curr = curr.next
        if not curr:
            print("Node not found")
        else:
            new_node = ListNode(value)
            new_node.next = curr.next
            curr.next = new_node

    '''
    # Work on this function

    def add_before(self, value, target):
        if not self.head:
            print("Linked List is empty")
            return
        if self.head.value == target:
            self.add_begin(value)
            return
        curr = self.head
        while curr.next is not None:
            if curr.next.value == target:
                break
            curr = curr.next
        if not curr:
            print("Node not found")
        else:
            new_node = ListNode(value)
            new_node.next = curr.next
            curr.next = new_node    
    ''' 

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_before(200,1000)
LL1.print_LL()