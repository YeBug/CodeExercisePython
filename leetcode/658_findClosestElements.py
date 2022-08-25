class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i, j = 0, len(arr) - k
        while i < j:
            mid = (i + j) // 2
            if x - arr[mid] > arr[mid + k] - x:
                i = mid + 1
            else:
                j = mid
        return arr[i:i+k]

if __name__ == "__main__":
    solution = Solution()
    arr = [1, 1, 2, 2, 2, 2, 2, 3, 3]
    k, x = 3, 3
    print(solution.findClosestElements(arr, k, x))