class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {}
        seen[0] = -1
        count = 0
        res = 0

        for right, value in enumerate(nums):
            count += 1 if value == 1 else -1
            if count in seen:
                res = max(res, right - seen[count])
            else:
                seen[count] = right
        
        return res

        