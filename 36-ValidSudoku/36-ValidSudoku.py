class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp1 = {}
        temp2 = {}
        temp3 = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] not in temp1 and board[i][j] != '.':
                    temp1[board[i][j]] = 1
                elif board[i][j] != '.':
                    return False
                if board[j][i] not in temp2 and board[j][i] != '.':
                    temp2[board[j][i]] = 1
                elif board[j][i] != '.':
                    return False
                # print(temp1, temp2)
            temp1 = {}
            temp2 = {}
        print("1, 2, Passsss")
        # temp1 = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in temp3[(i//3,j//3)]:
                    return False
                temp3[(i//3, j//3)].add(board[i][j])
        
        return True