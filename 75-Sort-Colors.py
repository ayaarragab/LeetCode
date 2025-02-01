from collections import Counter
class Solution(object):
    def sortColors(self, nums):
        \\\
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        \\\
        counts = Counter(nums)
        n_c = len(counts)
        s_indices = [sum(list(counts.values())[ : i + 1]) for i in range(n_c)]
        print(s_indices)
        for i in range(n_c - 1, -1, -1):
            if i - 1 <= 0:
                if i == n_c - 1:
                    s_indices[i] = s_indices[i - 1]
                else:
                    temp = s_indices[i]
                    s_indices[i] = s_indices[i - 1]
                    s_indices[i - 1] = temp
        s_indices[0] = 0
        i_s = 0
        for k, v in counts.items():
            for _ in range(v):
                if s_indices[i_s] < len(nums):
                    nums[s_indices[i_s]] = k
                    s_indices[i_s] += 1
            i_s += 1