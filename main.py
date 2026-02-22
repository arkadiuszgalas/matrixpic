import grid
matrix_len = len(grid.matrix)
matrix_len_in = len(grid.matrix[0])

print(str(matrix_len_in))

for i in range(matrix_len):
   print(grid.matrix[i][0], end ='')
