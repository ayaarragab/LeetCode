class Solution(object):
    def minSubArrayLen(self, target, nums):
        \\\
        :type target: int
        :type nums: List[int]
        :rtype: int
        \\\
        n = len(nums)
        if n == 0:
            return 0
        
        l = 0
        curr_sum = 0
        m_l = float('inf')
        
        for r in range(n):
            curr_sum += nums[r]
            
            while curr_sum >= target:
                m_l = min(m_l, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        
        return m_l if m_l != float('inf') else 0