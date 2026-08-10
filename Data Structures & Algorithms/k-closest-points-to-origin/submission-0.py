class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, point in enumerate(points):
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            distances.append((distance, i))

        heapq.heapify(distances)
        result = []
        while len(result) < k:
            _, i = heapq.heappop(distances)
            result.append(points[i])

        return result