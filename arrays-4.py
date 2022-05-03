# https://leetcode.com/problems/set-matrix-zeroes
def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col = set(),set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in col:
                    matrix[i][j] = 0
        
        return matrix
