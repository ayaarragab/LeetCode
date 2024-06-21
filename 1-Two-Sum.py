class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], i]

            num_to_index[num] = i

        if target == 0:
            if nums.count(0) == 2:
                idx = nums.index(0)
                return [idx, nums.index(0, idx + 1)]
            else:
                for num in nums:
                    if -num in nums:
                        return [nums.index(num), nums.index(-num)]   