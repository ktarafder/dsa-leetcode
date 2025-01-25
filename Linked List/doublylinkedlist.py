class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
# Write your code here
one = ListNode(1)
two = ListNode(2)
three = ListNode (3)
head = one
tail = three
one.next = two
two.prev = one
two.next = three
three.prev = two

# Foward traversal
curr = head 
while curr:
    if curr.next:
        print(f'{curr.val} <->', end=' ')
    else:
        print(f'{curr.val}', end=' ')
    curr = curr.next

print()
# Backwards traversal
curr = tail 
while curr:
    if curr.prev:
        print(f'{curr.val} <->', end=' ')
    else:
        print(f'{curr.val}', end=' ')
    curr = curr.prev
            