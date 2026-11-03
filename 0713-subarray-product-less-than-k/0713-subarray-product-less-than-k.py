class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        window = 1
        left = 0
        result = 0

        for right in range(len(nums)):
            window *= nums[right]
            while window >= k and left <= right:
                window //= nums[left]
                left += 1
            
            result += right - left + 1
        
        return result
        