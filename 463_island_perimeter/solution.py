def islandPerimeter(grid):
    wallLength=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                neighbours = [(x, y) for x in range(i-1, i+2) for y in range(j-1, j+2) if (abs(x - i) + abs(y-j) <= 1 and (x != i or y != j))]
                wallLength += 4 - len([neighbour for neighbour in neighbours if 0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(grid[0]) and grid[neighbour[0]][neighbour[1]]] )
    return wallLength


print(islandPerimeter([[0,1,0,0],
     [1,1,1,0],
      [0,1,0,0],
       [1,1,0,0]])) #16
print(islandPerimeter([[1]])) #4
print(islandPerimeter([[1, 1]])) #6
print(islandPerimeter([[]])) #6

