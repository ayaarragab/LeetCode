class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        n = 0
        for h in hours:
            if h >= target:
                n += 1
        return n