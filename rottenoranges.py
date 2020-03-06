

# Initialize the deck deque

numRow = len(grid)
numCol = len(grid[0])

queue = collections.deque()



# store the positions of rotten 
for r in range(numRow):
    for c in range(numCol):
        if grid[r][c] == 2:
            queue.append((r,c,0))


            


# find newighbours of rotten'
def neighbors(r,c):
    for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1):
            if 0<= nr < numRow and 0<= nc < numCol:
                yield nr,nc
                


# if the roten's neighbours have value 1, c=ange 2 and add the value there
while queue:
    r,c,d = queue.popleft()
    for  nr, nc in neighbors(r,c):
        if grid[nr][nc] == 1:
            grid[nr][nc] = 2
                queue.append((nr,nc,d+1))

