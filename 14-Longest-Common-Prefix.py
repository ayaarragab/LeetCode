class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length = len(min(strs))
        prefix = ""
        for i in range(min_length):
            current_char = strs[0][i]
            if all(string[i] == current_char for string in strs):
                prefix += current_char
            else:
                break
        return prefix