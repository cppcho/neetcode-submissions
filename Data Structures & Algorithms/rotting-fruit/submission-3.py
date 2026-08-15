class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRow = len(grid)
        numCol = len(grid[0])
    
        freshCount = 0
        q = deque() # (row, col, level)
    
        for r in range(numRow):
            for c in range(numCol):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))
        visited = set()
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        maxElapsed = 0
        while q:
            r, c, elapsed = q.popleft()
            maxElapsed = max(maxElapsed, elapsed)
            for d in dirs:
                nextR = r + d[0]
                nextC = c + d[1]
                if (
                    0 <= nextR < numRow and 0 <= nextC < numCol and
                    (nextR, nextC) not in visited and
                    grid[nextR][nextC] == 1
                ):
                    freshCount -= 1
                    visited.add((nextR, nextC))
                    q.append((nextR, nextC, elapsed + 1))
    
        if freshCount > 0:
            return -1
        return maxElapsed

        

    
        