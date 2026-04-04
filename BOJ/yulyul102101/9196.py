import sys

input = sys.stdin.read

def solve():
    data = input().split()
    
    bingo_board = {}
    idx = 0
    for r in range(5):
        for c in range(5):
            num = int(data[idx])
            bingo_board[num] = (r, c)
            idx += 1
            
    calls = list(map(int, data[25:]))
    marked = [[0] * 5 for _ in range(5)]
    
    def count_bingo():
        line_count = 0
        
        for r in range(5):
            if sum(marked[r]) == 5:
                line_count += 1
        
        for c in range(5):
            col_sum = 0
            for r in range(5):
                col_sum += marked[r][c]
            if col_sum == 5:
                line_count += 1
                
        diag1 = 0
        for i in range(5):
            diag1 += marked[i][i]
        if diag1 == 5:
            line_count += 1
            
        diag2 = 0
        for i in range(5):
            diag2 += marked[i][4-i]
        if diag2 == 5:
            line_count += 1
            
        return line_count

    for i in range(len(calls)):
        num = calls[i]
        r, c = bingo_board[num]
        marked[r][c] = 1
        
        if i >= 11:
            if count_bingo() >= 3:
                print(i + 1)
                return

if __name__ == "__main__":
    solve()