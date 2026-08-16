class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sintervals = sorted(intervals, key=lambda x: x[0])
        res = [sintervals[0]]
        for i in range(1, len(intervals)):
            last_interval = res[-1]
            curr_interval = sintervals[i]
            if curr_interval[0] > last_interval[1]:
                res.append(curr_interval)
            else:
                last_interval[1] = max(last_interval[1], curr_interval[1])
        return res

        