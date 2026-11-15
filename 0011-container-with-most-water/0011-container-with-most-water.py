class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        window = 0

        left = 0
        right = len(height) - 1
        while(left < right):
            window = min(height[left], height[right]) * (right - left)
            result = max(result, window)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1


        return result
        