from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        result = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        current_sum = 0

        for n in nums:
            current_sum += n
            result += prefix[current_sum - k]
            prefix[current_sum] += 1


        return result