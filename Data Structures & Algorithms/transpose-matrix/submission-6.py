class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #[[2,1],[-1,3]]
        col=len(matrix[0]) #3
        rows=len(matrix) #2
        l=[]
        for i in range(col):
            l1=[]
            for j in range(rows):
                l1.append(0)
            l.append(l1)
        for i in range(rows):
            for j in range(col):
                l[j][i] = matrix[i][j]

        return l