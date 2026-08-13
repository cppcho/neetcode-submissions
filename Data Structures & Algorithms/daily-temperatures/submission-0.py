class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        dq = deque() # temperature : index
        for i, t in enumerate(temperatures):
            while dq and dq[0][0] < t:
                _, j = dq.popleft()
                res[j] = i - j
            dq.appendleft((t, i))
        return res



        