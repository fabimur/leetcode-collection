class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        window = 0
        min_len = float('inf')
        left = 0

        for right in range(len(nums)):
            window += nums[right]

            while window >= target:
                min_len = min(min_len, right - left + 1)
                window -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0