class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        longestC = 0
        length = 0
        for n in nums:
            if (n - 1) not in nums:
                length = 0
                while (n + length) in nums:
                    length += 1
            longestC = max(length, longestC)
        return longestC