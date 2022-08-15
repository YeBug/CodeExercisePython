class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        strs = str(self.val)
        cur = self.next
        while cur:
            strs += "->{}".format(cur.val)
            cur = cur.next
        return strs


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        head.next.next = self.swapPairs(head.next.next)
        new_head = head.next
        head.next = head.next.next
        new_head.next = head
        return new_head

if __name__ == "__main__":
    head = Node(0)
    cur = head
    for i in range(1, 10):
        cur.next = Node(i)
        cur = cur.next
    print(head.next)
    solution = Solution()
    print(solution.swapPairs(head.next))