class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        arr = []
        for i, w in enumerate(words):
            if x in w:
                arr.append(i)
        return arr