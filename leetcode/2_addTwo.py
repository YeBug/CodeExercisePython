"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

----------------------------------------------------

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""
class ListNode(object):
     def __init__(self, val=0, next_=None):
         self.val = val
         self.next = next_

     def __str__(self):
         strs = ""
         cur = self
         while cur:
             strs += str(cur.val)
             cur = cur.next
         return strs


class Solution:
    def addTwoNumbers(self, l1, l2):
        return self.addTwo(l1, l2, 0)

    def addTwo(self, l1, l2, add):
        if not (l1 and l2):
            return None if add == 0 else ListNode(add)
        val1 = 0 if l1 == None else l1.val
        val2 = 0 if l2 == None else l2.val
        sums = val1 + val2 + add
        add = 0
        if sums > 9:
            sums = sums % 10
            add = 1
        ans = ListNode(sums)
        ans.next = self.addTwo(None if not l1 else l1.next, None if not l2 else l2.next, add)
        return ans

if __name__ == "__main__":
    solution = Solution()
    L1 = [2, 4, 3]
    L2 = [5, 6, 4]
    head1 = ListNode(0)
    head2 = ListNode(0)
    cur = head1
    for i in L1:
        cur.next = ListNode(i)
        cur = cur.next
    cur = head2
    for i in L2:
        cur.next = ListNode(i)
        cur = cur.next

    print(solution.addTwoNumbers(head1.next, head2.next))
