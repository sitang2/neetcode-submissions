class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #rotate corners
        #(0, 0) -> (0, n) -> (n, n) ->(n, 0)
        #rotate diamond
        #(0, 1) -> (n, 1 + n) -> (1 + n, n) ->(1, 0)

        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]