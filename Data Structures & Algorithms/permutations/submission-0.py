class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
            return
        backtrack([])
        return res
        