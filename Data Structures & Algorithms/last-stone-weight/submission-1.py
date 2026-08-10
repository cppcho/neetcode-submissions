class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -1 * s for s in stones ]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)
            if x == y:
                continue
            
            if x < y:
                heapq.heappush(stones, x - y)
            else:
                heapq.heappush(stones, y - x)

        if not stones:
            return 0
        return stones[0] * -1
                
