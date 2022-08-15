"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

------------------------------------------------------------

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
class Solution:

    def lengthOfLongestSubstring(self, s):
        map_ = set()
        i, j, ans = 0, 0, 0
        for c in s:
            while (c in map_):
                map_.remove(s[i])
                i += 1
            map_.add(c)
            ans = j - i + 1 if ans < j - i + 1 else ans
            j += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))