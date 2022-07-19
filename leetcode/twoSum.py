"""

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

--------------------------------------------------------

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

"""


class Solution:
    def __init__(self):
        self.rest_dic = dict()

    def two_sum(self, nums, target):
        for i in range(len(nums)):
            if target-nums[i] in self.rest_dic.keys():
                return {i, self.rest_dic[target-nums[i]]}
            self.rest_dic[nums[i]] = i
        return {0, 0}


if __name__ == "__main__":
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 26))