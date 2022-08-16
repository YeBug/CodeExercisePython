class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        x_ = self.myPow(x, n // 2)
        if n % 2 == 1:
            return x * x_ * x_
        return x_ * x_

if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(2, 10))