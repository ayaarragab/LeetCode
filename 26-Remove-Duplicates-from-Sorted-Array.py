class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if not nums or length == 1:
            return length
        i = 1
        new_length = length
        while i < new_length:
            while i < new_length and nums[i] == nums[i - 1]:
                nums.pop(i)
                new_length = len(nums)
            i += 1
        return new_length
