class Solution:
    dp = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = {}
        return self.solve(coins, amount)

    def solve(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in self.dp:
            return self.dp[amount]

        res = -1
        for coin in coins:
            r = self.solve(coins, amount - coin)
            if r == -1:
                continue
            if res != -1:
                res = min(res, r + 1)
            else:
                res = r + 1
        self.dp[amount] = res
        return res
                

        


