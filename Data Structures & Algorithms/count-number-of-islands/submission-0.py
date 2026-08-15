class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    res += 1
                    self.backtrack(grid, row, col)
        return res

        
    def backtrack(self, grid, row: int, col: int):
        if row < 0 or row >= len(grid):
            return
        if col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == '0' or grid[row][col] == '-1':
            return
        grid[row][col] = '-1'
        self.backtrack(grid, row-1, col)
        self.backtrack(grid, row, col-1)
        self.backtrack(grid, row+1, col)
        self.backtrack(grid, row, col+1)
