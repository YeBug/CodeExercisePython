class Solution(object):
    def uniquePaths(self, m, n):
        arr = [[0 for i in range(n)] for j in range(m)]
        arr[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    arr[i][j] += arr[i-1][j]
                if j > 0:
                    arr[i][j] += arr[i][j-1]
        return arr[m-1][n-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3, 7))