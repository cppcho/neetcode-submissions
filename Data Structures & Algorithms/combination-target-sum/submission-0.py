class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(curr_target, selected):
            if curr_target < 0:
                return
            if curr_target == 0:
                res.append(list(selected))
                return
            for n in nums:
                if selected and n < selected[-1]:
                    continue
                selected.append(n)
                backtrack(curr_target - n, selected)
                selected.pop()
            return
        backtrack(target, [])
        return res
            

    