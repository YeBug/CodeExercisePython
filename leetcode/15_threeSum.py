class Solution(object):
    def threeSum(self, nums):
        lens = len(nums)
        ans = []
        nums.sort()
        if lens < 3:
            return ans
        for i in range(lens):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = lens - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(nums))