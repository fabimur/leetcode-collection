class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: 0}      # prefijo -> primer left posible
        prefix = 0
        res = 0

        for right, value in enumerate(nums):
            prefix += 1 if value == 1 else -1
            if prefix in seen:
                res = max(res, right - seen[prefix] + 1)
            else:
                seen[prefix] = right + 1
        
        return res