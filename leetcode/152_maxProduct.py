class Solution(object):
    def maxProduct(self, nums):
        mininum, maxnum, ans = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            min_, max_ = mininum, maxnum
            mininum = min(max_ * i, min(i, min_ * i))
            maxnum = max(min_ * i, max(i, max_ * i))
            ans = max(maxnum, ans)
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2,3,-2,4]))