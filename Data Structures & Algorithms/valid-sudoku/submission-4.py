class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #no duplicates in square
        for i in range(9):
            currentset=set()
            for r in range(3):
                for c in range(3):
                    row=(i//3) * 3 + r
                    col =(i%3) * 3 + c
                    if board[row][col]==".":
                        continue
                    if board[row][col] in currentset:
                        return False 
                    currentset.add(board[row][col])
            
        #no duplicates in row
       
        for i in range(9):
            newarray=set()

            for j in range(9):

                if board[i][j]==".":
                    continue
                elif board[i][j] in newarray:
                    return False 
                
                newarray.add(board[i][j]) 
                
        #no duplicates in coloumn 

        for coloumns in range(9):

            newarray1=set()

            for c in range(9):

                if board[c][coloumns]==".":
                    continue
                elif board[c][coloumns] in newarray1:
                    return False 
                newarray1.add(board[c][coloumns]) 

        return True

        