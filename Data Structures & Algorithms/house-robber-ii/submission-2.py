class Solution:
    dp = {}
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.dp = {}
        a = self.solve(nums, 0, len(nums) - 1)
        self.dp = {}
        b = self.solve(nums, 1, len(nums))
        return max(a, b)


    def solve(self, nums, start, end):
        if start >= end:
            return 0
        if start in self.dp:
            return self.dp[start]
        
        self.dp[start] = max(
            self.solve(nums, start + 1, end),
            nums[start] + self.solve(nums, start + 2, end)
        )
        return self.dp[start]