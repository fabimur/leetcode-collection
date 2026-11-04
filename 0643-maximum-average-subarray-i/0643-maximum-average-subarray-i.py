class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_window = float('-inf')
        window = 0

        left = 0
        for right in range(len(nums)):
            window += nums[right]

            if right - left + 1 > k:
                window -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_window = max(max_window, window)

        return max_window/k

        