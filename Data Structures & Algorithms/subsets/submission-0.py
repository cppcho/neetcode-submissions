class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(tar_len, curr_path, i):
            if len(curr_path) == tar_len:
                res.append(list(curr_path))
                return

            for i in range(i, len(nums)):
                n = nums[i]
                curr_path.add(n)
                backtrack(tar_len, curr_path, i+1)
                curr_path.remove(n)
        
        for i in range(len(nums) + 1):
            backtrack(i, set(), 0)

        return res
