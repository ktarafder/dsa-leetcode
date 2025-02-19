class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head, n):
  if n == 0:
    return head
  curr = head
  len = 0
  while curr:
    len += 1
    curr = curr.next
  if len == n:
    return head.next
  curr = head
  prev = None
  for _ in range(len-n):
    prev = curr
    curr = curr.next
  prev.next = curr.next
  return head
    

one = ListNode(1) ; one.next = ListNode(2) ; one.next.next = ListNode(3) ; one.next.next.next = ListNode(4) ; one.next.next.next.next = ListNode(5)
res = solve(one, 2)

def print_LL(head):
  if not head:
    print("Linked List is empty")
  else:
    curr = head
    while curr:
      if not curr.next:
        print(curr.val) ; break # pls dont smite me for this, Python creators
      print(curr.val, end=" -> ")
      curr = curr.next

print_LL(res)

'''
Same as my solution, but it uses a dummy node 
this one is more creative, this is taken from leetle site
its more appropiate to call the first variable curr here rather than first
since no pointers are being used
'''

def solve(head, n):
    dummy = ListNode(0)
    dummy.next = head
    length = 0
    first = head
    while first:
        length += 1
        first = first.next
    length -= n
    first = dummy
    while length > 0:
        length -= 1
        first = first.next
    first.next = first.next.next
    return dummy.next

'''
Two pointer approach
'''

def solve(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy
    
    for _ in range(n+1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next
              