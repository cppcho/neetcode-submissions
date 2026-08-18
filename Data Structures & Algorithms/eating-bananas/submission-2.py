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

        left, right = 1, max_pile
        while left <= right:
            mid = (left + right) // 2
            hours = hours_for_k(mid)
            if hours <= h and (mid <= 1 or hours_for_k(mid-1) > h):
                return mid
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return -1
