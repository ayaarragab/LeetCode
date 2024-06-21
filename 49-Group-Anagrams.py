class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = dict()
        for string in strs:
            sortedStr = ''.join(sorted(string))
            if sortedStr in hashMap: # Avoid using .keys() for better performance
                hashMap[sortedStr].append(string)
            else:
                hashMap[sortedStr] = [string]
        return list(hashMap.values())