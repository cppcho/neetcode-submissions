"""
1 1 3 3
1 x 3 x
x 1 x 3

2 9 3 8 6
  x   x
x   x   x

2 9 3 8 6

rob(nums[1:]) 2 + rob(nums[2:])
"""
class Solution:
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


        