class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        window = 0
        min_window = float('inf')

        left = 0
        for right in range(len(nums)):
            window += nums[right]

            if window >= target:
                while window >= target:
                    window -= nums[left]
                    left += 1

                min_window = min(min_window, (right - left + 1) + 1)

        return min_window if min_window != float('inf') else 0
        