class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for s in strs:
            stre = ''.join(sorted(s))
            if stre not in anagrams:
                anagrams[stre] = []
            anagrams[stre].append(s)
        return list(anagrams.values())