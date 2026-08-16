"""
1 2 3 1

dp = [0 0 0 0 0 0 0]

rob(nums[1:]) 2 + rob(nums[2:])
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
"""
    dp = {}
    def rob(self, nums: List[int]) -> int:
        self.dp = {}
        return self.solve(nums, 0)


    def solve(self, nums, start):
        if start >= len(nums):
            return 0
        if start in self.dp:
            return self.dp[start]
        
        self.dp[start] = max(
            self.solve(nums, start + 1),
            nums[start] + self.solve(nums, start + 2)
        )
        return self.dp[start]
"""