class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m = len(board)
        n = len(board[0])

        def backtrack(i, j, pathSet):
            path_len = len(pathSet)
            if path_len == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if (i, j) in pathSet:
                return False
            if word[path_len] != board[i][j]:
                return False

            pathSet.add((i, j))
            for direction in directions:
                x, y = (i + direction[0], j + direction[1])
                if backtrack(x, y, pathSet):
                    return True
            pathSet.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, set()):
                    return True
        return False




        