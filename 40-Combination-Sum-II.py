from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start, comb, total):
            if total == target:
                res.append(comb[:])
                return
            elif total > target:
                return
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, comb, total + candidates[i])
                comb.pop()
                prev = candidates[i]
        backtrack(0, [], 0)
        return res