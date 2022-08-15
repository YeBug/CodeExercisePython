class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left, right = 0, 0
        while left <= right:
            if left + nums[left] >= right:
                right = left + nums[left]
                if right >= len(nums)-1:
                    return True
            left += 1
        return False

if __name__ == "__main__":
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]
    solution = Solution()
    print("ans1 = {}; ans2 = {}".format(solution.canJump(nums1), solution.canJump(nums2)))