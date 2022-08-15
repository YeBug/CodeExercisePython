class Solution(object):
    def removeDuplicates(self, nums):
        lens = len(nums)
        i = 0
        while i < lens:
            j = i
            while j < lens and nums[j] == nums[i]:
                j += 1
            j -= 1
            lens -= j-i
            del nums[i:j]
            i += 1
        return lens

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_nums = [0, 1, 2, 3, 4]
    solution = Solution()
    k = solution.removeDuplicates(nums)
    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]
    print("pass")