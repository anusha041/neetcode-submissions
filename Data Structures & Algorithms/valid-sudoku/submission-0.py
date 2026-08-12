class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for i in range (9):
            boardd = sorted(board[i])
            j= 8
            while boardd[j] != "." and j>0:
                if boardd[j] == boardd[j-1]:
                    return False
                j=j-1
        #check column
        a = {}
        for i in range (9):
            for j in range (9):
                if board [j][i] != ".":
                    a[board[j][i]] = 1 + a.get(board[j][i], 0)
                    if a[board[j][i]] > 1:
                        return False
            a= {}
        
        #check boxes 
        b = {}
        for i in range (2, 9, 3):
            for j in range (2, 9, 3):
                for k in range (i-2, i+1):
                    for l in range (j-2, j+1):
                        if board[k][l] != ".":
                            b[board[k][l]] = 1 + b.get(board[k][l], 0)
                            if b[board[k][l]] > 1:
                                return False
                b = {}
        return True







            

        