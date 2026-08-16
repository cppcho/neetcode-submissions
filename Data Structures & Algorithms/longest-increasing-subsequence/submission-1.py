class Solution:
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
        print(memo)
        return res




