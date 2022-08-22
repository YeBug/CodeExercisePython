class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def getHeight(root, height):
            if root:
                height += 1
                height = max(getHeight(root.left, height), getHeight(root.right, height))
            return height

        height = getHeight(root, -1)
        result = [["" for i in range(pow(2, height + 1) - 1)] for j in range(height + 1)]

        def putInto(root, row, col):
            if root and row < len(result) and col < len(result[0]):
                result[row][col] = "{}".format(root.val)
                putInto(root.left, row + 1, col - pow(2, height - row - 1))
                putInto(root.right, row + 1, col + pow(2, height - row - 1))

        putInto(root, 0, len(result[0]) // 2)
        return result