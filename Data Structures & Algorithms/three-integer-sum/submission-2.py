class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] 
                if s == -a:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s > -a:
                    right -= 1
                else:
                    left += 1
        return list(res)
                