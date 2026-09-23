class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=defaultdict(set)        #creates a dictionary with empty key values that can be entered later, makes it a set so that there are no dupes
        rows=defaultdict(set)
        squares=defaultdict(set) # key= (row/3, col/3)            main trick 

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif (board[r][c] in rows[r]) or (board[r][c] in col[c]) or (board[r][c] in squares[r//3,c//3]):  #check if its in the row or col at once 
                    return False 

                col[c].add(board[r][c])                                     #add 
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        
        return True 