class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxi = len(sentences[0].split())

        for s in sentences:
            n = len(s.split())
            maxi = maxi if maxi >= n else n
        return maxi