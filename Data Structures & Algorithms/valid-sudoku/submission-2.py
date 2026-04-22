class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        columns = [["."]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                columns[i][j] = board[j][i]

        boxes = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i<=2:
                    if j<=2:
                        boxes[0].append(board[i][j])
                    elif j<=5:
                        boxes[1].append(board[i][j])
                    else:
                        boxes[2].append(board[i][j])
                elif i<=5:
                    if j<=2:
                        boxes[3].append(board[i][j])
                    elif j<=5:
                        boxes[4].append(board[i][j])
                    else:
                        boxes[5].append(board[i][j])
                else:
                    if j<=2:
                        boxes[6].append(board[i][j])
                    elif j<=5:
                        boxes[7].append(board[i][j])
                    else:
                        boxes[8].append(board[i][j])

        new_board = board+columns+boxes
        
        for i in range(len(new_board)):
            digits = [str(i) for i in range(1,10)]
            for j in range(n):
                if new_board[i][j].isdigit():
                    if new_board[i][j] not in digits:
                        return False
                    else:
                        digits.remove(new_board[i][j])

        return True