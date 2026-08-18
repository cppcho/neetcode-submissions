class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m = len(board)
        n = len(board[0])

        def backtrack(path):
            path_len = len(path)
            if path_len == len(word):
                return True

            # path_len < len(word)
            for direction in directions:
                x, y = (path[-1][0] + direction[0], path[-1][1] + direction[1])
                if (x, y) in path:
                    continue
                if 0 <= x < m and 0 <= y < n:
                    if board[x][y] == word[path_len]:
                        path.append((x, y))
                        if backtrack(path):
                            return True
                        del path[-1]
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack([(i, j)]):
                    return True
        return False




        