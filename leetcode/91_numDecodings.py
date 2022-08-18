class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1 if int(s[0]) != 0 else 0
        for i in range(1, len(s)):
            if int(s[i]) > 0:
                dp[i+1] = dp[i]
            if int(s[i]) + int(s[i-1]) * 10 <= 26 and int(s[i-1]) != 0:
                dp[i+1] += dp[i-1]
        return dp[len(s)]

if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings("123456"))