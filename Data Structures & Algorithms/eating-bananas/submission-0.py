"""
n <= h

1,2,3,4

blute force
- for each k (1.. max(piles[i]))
    sum = 0
    for each i, 
        sum += (piles[i] // k + 1)
    if sum > h
        return k

many  n

k  > n


"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        max_pile = max(piles)

        # how many hours take me if i can eat k bananas per hour
        def hours_for_k(k):
            res = 0
            for pile in piles:
                res += ((pile-1) // k) + 1
            return res

        for k in range(1, max_pile + 1):
            hour = hours_for_k(k)
            if hour <= h:
                return k
        return -1
