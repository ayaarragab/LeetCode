class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        if not nums:
            return 0
        max_streak = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                streak = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    streak += 1
                max_streak = max(max_streak, streak)
        return max_streak

