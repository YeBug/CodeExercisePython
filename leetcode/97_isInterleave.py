class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1)):
            if s3[i] == s1[i]:
                dp[i + 1][0] = True
            else:
                break
        for i in range(len(s2)):
            if s3[i] == s2[i]:
                dp[0][i + 1] = True
            else:
                break
        for i in range(len(s1)):
            for j in range(len(s2)):
                if dp[i + 1][j] and s2[j] == s3[i + j + 1] \
                        or dp[i][j + 1] and s1[i] == s3[i + j + 1]:
                    dp[i + 1][j + 1] = True
        return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    solution = Solution()
    s1 = "aa"
    s2 = "d"
    s3 = "aad"
    solution.isInterleave(s1, s2, s3)
