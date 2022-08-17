class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        small_head = ListNode()
        big_head = ListNode()
        small_cur = small_head
        big_cur = big_head
        while head:
            if head.val >= x:
                big_cur.next = head
                head = head.next
                big_cur = big_cur.next
            else:
                small_cur.next = head
                head = head.next
                small_cur = small_cur.next
        small_cur.next = big_head.next
        big_cur.next = None
        return small_head.next