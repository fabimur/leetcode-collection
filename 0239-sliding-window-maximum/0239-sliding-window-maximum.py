from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()   # índices, con valores decrecientes
        res = []

        for i, x in enumerate(nums):
            # 1. quitar del final los que son menores que x (nunca serán máximo)
            while dq and nums[dq[-1]] < x:
                dq.pop()
                
            dq.append(i)

            # 2. quitar del frente si se salió de la ventana
            if dq[0] <= i - k:
                dq.popleft()

            # 3. si ya hay ventana completa, el frente es el máximo
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res