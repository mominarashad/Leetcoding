class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        row_begin=0
        col_begin=0

        col_end=len(matrix[0])-1
        row_end=len(matrix)-1

        res=[]

        while row_begin<=row_end and col_begin<=col_end:

            for i in  range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])

            row_begin+=1


            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])

            col_end-=1
            if row_end>=row_begin:
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])

            row_end-=1
           
            if col_end>=col_begin:
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])

            col_begin+=1

        return res