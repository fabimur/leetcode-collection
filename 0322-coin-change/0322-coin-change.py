class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins = set(coins)
        dp = [0] + [amount + 1] * amount

        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                for c in coins:
                    if c <= i:
                        dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1