class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        node = self
        strs = ""
        while node:
            strs += str(node.val)
            node = node.next
            if node:
                strs += ", "
        return strs

class Solution:
    def rotateRight(self, head, k):
        if not head or not k:
            return head
        lens = 1
        cur = head
        while cur.next:
            cur = cur.next
            lens += 1
        k = k % lens
        if not k:
            return head
        cur.next = head
        i, cur = lens - k, head
        while i > 1:
            cur = cur.next
            i -= 1
        new_head = cur.next
        cur.next = None
        return new_head

    def buildRangeList(self, val):
        node = Node(0)
        cur = node
        for i in range(1, val+1):
            cur.next = Node(i)
            cur = cur.next
        return node.next

if __name__ == "__main__":
    solution = Solution()
    print(solution.rotateRight(solution.buildRangeList(5), 3))