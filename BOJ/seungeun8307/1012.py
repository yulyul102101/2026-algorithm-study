import sys
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

def dfs(arr, x, y, n, m): 
    arr[x][y] = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                dfs(arr, nx, ny, n, m)

for _ in range(T):
    n, m, k = map(int, sys.stdin.readline().split())
    nm = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        nm[x][y] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if nm[i][j] == 1:
                dfs(nm, i, j, n, m)
                count += 1
    
    print(count)