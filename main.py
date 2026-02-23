import grid

grid_height = len(grid.matrix)
grid_width = len(grid.matrix[0])

print(f"Matrix after transposition has dimensions: {grid_width}x{grid_height}")

for i in range(grid_width):
   for j in range(grid_height):
      print(grid.matrix[j][i], end ='')
   print("")
