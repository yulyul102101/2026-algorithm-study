def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    num = 1
    r, c = 0, 0
    dr, dc = 0, 1
    
    for _ in range(n*n):
        answer[r][c] = num
        num += 1
        
        nr, nc = r+dr, c+dc
        
        if not (0 <= nr < n and 0 <= nc < n and answer[nr][nc] == 0):
            dr, dc = dc, -dr
            nr, nc = r + dr, c + dc
            
        r, c = nr, nc
        
    return answer