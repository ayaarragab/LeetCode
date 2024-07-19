class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        length = len(nums)
        i = 0
        j = n
        while (i < n and j < length):
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res