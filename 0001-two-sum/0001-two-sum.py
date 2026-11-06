class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = defaultdict(int)

        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i

        return []

            
