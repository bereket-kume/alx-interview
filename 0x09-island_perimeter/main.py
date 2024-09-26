grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
row = len(grid)
column = len(grid[0])
count = 0

for i in range(row):
    for j in range(column):
        if grid[i][j] == 1:
            if grid[i -1 ][j] == 0 or i ==  0:
                count += 1

            if grid[i+1][j] == 0 or i == 0:
                count += 1
            if grid[i][j-1] == 0 or j == 0:
                count += 1
        
            if grid[i][j+1] == 0 or (column - j) == 1:
                count += 1
print(count)