class Solution:
    def aux(self, coins: list[int], amount: int, memo: dict) -> int:
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]

        best = float('inf')
        for value in coins:
            best = min(best, 1 + self.aux(coins, amount - value, memo))

        memo[amount] = best
        return best

    def coinChange(self, coins: list[int], amount: int) -> int:
        res = self.aux(coins, amount, {})
        return res if res != float('inf') else -1