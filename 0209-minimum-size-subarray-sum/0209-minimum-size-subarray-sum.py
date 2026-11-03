class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        result = float('inf')
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                result = min(result, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return result if result != float('inf') else 0