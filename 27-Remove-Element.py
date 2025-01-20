class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        numOcc = 0
        for num in nums:
            if num == val:
                numOcc += 1
        for i in range(numOcc):
            for i, num in enumerate(nums):
                if num == val:
                    del nums[i]
        return len(nums)