class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            s = set()
            for j in range(9):
                digit = board[i][j]
                if digit != '.' and digit in s:
                    return False
                s.add(digit)

        # cols
        for i in range(9):
            s = set()
            for j in range(9):
                digit = board[j][i]
                if digit != '.' and digit in s:
                    return False
                s.add(digit)

        # 3x3 grid
        for i in range(3):
            for j in range(3):
                s = set()
                for x in range(3):
                    for y in range(3):
                        digit = board[x + 3*i][y + 3*j]
                        if digit != '.' and digit in s:
                            return False
                        s.add(digit)

        for i in range(9):
            s = set()
            for j in range(9):
                digit = board[(j//3) + 3*(i//3)][(j%3) + 3*(i%3)]
                if digit != '.' and digit in s:
                    return False
                s.add(digit)

        return True