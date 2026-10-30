class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        suffix = 1
        for i in range(len(nums)):
            result[i] *= suffix
            suffix *= nums[i]

        prefix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= prefix
            prefix *= nums[i]
        
        return result
