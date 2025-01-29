class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_ = sum(accounts[0])
        for arr in accounts:
            curr_sum = sum(arr)
            max_ = max_ if max_ >= curr_sum else curr_sum
        return max_