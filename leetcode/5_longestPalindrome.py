import numpy as np

class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        dp = np.diag(np.ones(len(s), dtype=int))
        al, ar = 0, 0
        for r in range(1, len(s)):
            for l in range(r):
                if s[l] != s[r]:
                    continue
                elif r - l == 1 or dp[l + 1][r - 1]:
                    dp[l][r] = 1
                    if ar - al < r - l:
                        al, ar = l, r
        return s[al:ar + 1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("asdsabbasdvvv12v2vvvv"))
