class Solution:
    def generateParenthesis(self, n):
        def build(left, right, str):
            if left == 0:
                for i in range(right):
                    str += ")"
                ans.append(str)
                return
            str += "("
            build(left-1, right, str)
            if left < right:
                str = str[:-1]
                str += ")"
                build(left, right-1, str)
        ans = []
        build(n, n, "")
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(5))