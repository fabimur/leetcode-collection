class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        valid_windows = 0
        window = 1
        left = 0
        for right in range(len(nums)):
            window *= nums[right]
            while window >= k:
                window //= nums[left]
                left += 1
            valid_windows += right - left + 1

        return valid_windows