class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_w = 0
        for s in sentences:
            max_w = max(max_w, len(s.split()))
        return max_w
