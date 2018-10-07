from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

global visited
visited = set([])

def startingPosition(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 'P':
        return (i,j)


def senseTrap(grid, x, y):
  if grid[x + 1][y] == 'T':
    return True
    
  if grid[x][y + 1] == 'T':
    return True
    
  if grid[x - 1][y] == 'T':
    return True
    
  if grid[x][y - 1] == 'T':
    return True
    

def traverse(grid, x, y):
  
  if (x,y) in visited or grid[x][y] == "#":
    return 0
  
  visited.add((x,y))
  cur = 0
    
  if (grid[x][y] == 'G'):
    if (senseTrap(grid, x, y)):
      return 1
    else:
      cur = 1
  else:
    if (senseTrap(grid, x, y)):
      return 0
    
  return cur + traverse(grid, x + 1, y) + traverse(grid, x, y + 1)        + traverse(grid, x - 1, y) + traverse(grid, x, y -1)
  
grid = []  
  
for i in stdin:
  grid.append(i.strip())
  


grid.pop(0)

y, x = startingPosition(grid)

print(traverse(grid, y, x))


