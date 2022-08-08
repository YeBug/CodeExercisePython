class Solution(object):
    def maxSubArray(self, nums):
        ans = nums[0]
        cur = 0
        for i in nums:
            cur = cur + i if cur + i > i else i
            ans = cur if cur > ans else ans
        return ans

if __name__ == "__main__":
    arrs = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(arrs))