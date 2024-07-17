class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = []
        number = ''.join([str(d) for d in digits])
        numberp = int(number) + 1
        for c in str(numberp):
            l.append(int(c))
        return l