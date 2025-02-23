class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(perms, nums, pick):
            if len(perms) == len(nums):
                res.append(perms.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perms.append(nums[i])
                    pick[i] = True
                    backtrack(perms, nums, pick)
                    perms.pop()
                    pick[i] = False
        backtrack([], nums, [False] * len(nums))
        return res