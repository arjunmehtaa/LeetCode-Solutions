class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]: 
        ans = []
        for j in range(0, len(matrix[0])):
            column = []
            for i in range(0, len(matrix)):
                column.append(matrix[i][j])
            ans.append(column)
        return ans