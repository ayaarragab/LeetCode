class Solution(object):
    def containsDuplicate(self, nums):
        \\\
        :type nums: List[int]
        :rtype: bool
        \\\
        f = {}
        for num in nums:
            if num in f:
                return True
            f[num] = 1
        return False