// Last updated: 3/17/2025, 11:10:45 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if elem != '.':
                    res += [(i, elem), (elem, j), (i // 3, j//3, elem)]
        print(set(res))
        return len(res) == len(set(res))

        