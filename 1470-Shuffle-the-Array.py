class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr1 = []
        arr2 = []
        res = []
        length = len(nums)
        for i in range(0, n):
            arr1.append(nums[i])
        for j in range(n, length):
            arr2.append(nums[j])
        for idx in range(0, n):
            res.append(arr1[idx])
            res.append(arr2[idx])
        return res