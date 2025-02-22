class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        arrangement = []

        def dfs(idx, current_sum):
            if current_sum == target:
                combinations.append(arrangement.copy())
                return
            if current_sum > target or idx >= len(candidates):
                return  #

            arrangement.append(candidates[idx])
            dfs(idx, current_sum + candidates[idx])

            arrangement.pop()

            dfs(idx + 1, current_sum)

        dfs(0, 0)
        return combinations
