import heapq

def distance(x, y):
    return sqrt((x * x) + (y * y))

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dict_for_di_per_p = {}
        for p in points:
            di = distance(p[0], p[1])
            if di not in dict_for_di_per_p.keys():
                dict_for_di_per_p[di] = [p]
            else:
                dict_for_di_per_p[di].append(p)
        d_list = [key for key in dict_for_di_per_p.keys()]
        heapq.heapify(d_list)
        out = []
        if len(d_list) == 1:
            for i in range(0, k):
                out.append(dict_for_di_per_p[d_list[0]][i])
            return out
        for _ in range(k):
            key = heapq.heappop(d_list)
            for p in dict_for_di_per_p[key]:
                out.append(p)
            if len(out) == k:
                break
        return out