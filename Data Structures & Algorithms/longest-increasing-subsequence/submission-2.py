class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(nums):
                return 0
            if (i, j) in memo:
                return memo[i, j]

            lis = dfs(i + 1, j)   
            if j == -1 or nums[j] < nums[i]:
                lis = max(dfs(i + 1, i) + 1, lis)
            
            memo[i, j] = lis
            return lis
        return dfs(0, -1)
        
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        memo = [0] * len(nums)
        for i, num in enumerate(nums):
            lmax = 0
            for j in range(i):
                if nums[j] < num:
                    lmax = max(memo[j], lmax)
            memo[i] = lmax + 1
            res = max(res, memo[i])
        return res
    """