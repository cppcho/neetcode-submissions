class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c]+1)
        if dp[amount] > amount:
            return -1
        return dp[amount]



    dp = {}
    def coinChange2(self, coins: List[int], amount: int) -> int:
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
                

        


