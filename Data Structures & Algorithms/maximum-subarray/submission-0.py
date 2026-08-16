class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        local_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            res = max(res, local_max)
        return res

        