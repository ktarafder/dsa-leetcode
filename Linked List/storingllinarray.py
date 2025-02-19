class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# this will just append the entire ll from curr listnode to rest of the linked list nodes
def lltoarr(head):
    curr = head
    res = [] 
    while curr:
        res.append(curr)
        curr = curr.next
    return res

# without the links
def lltoarr2(head):
    curr = head
    res = [] 
    while curr:
        new_node = ListNode(curr.val)
        res.append(new_node)
        curr = curr.next
    return res

one = ListNode(1) ; one.next = ListNode(2) ; one.next.next = ListNode(3) ; one.next.next.next = ListNode(4) ; one.next.next.next.next = ListNode(5)
result = lltoarr(one)
result2 = lltoarr2(one)

'''
The first function whose return val is stored in result, contains both the ListNode value
but also the rest of the Linked List from that node within each object in the array
'''
for node in result:
    curr = node
    while curr:
        print(node.val, end=" ")
        curr = curr.next
print()

'''
The second function whose return val is stored in result2 contains only the ListNode
object with only the ListNode's value, and no links within each object in the array
'''
for node in result2:
    print(node.val, end=' ')

print()
for node in result2:
    curr = node
    while curr:
        print(node.val, end=" ")
        curr = curr.next