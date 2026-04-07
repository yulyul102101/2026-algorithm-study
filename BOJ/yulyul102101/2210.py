import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    board = []
    for i in range(0, 25, 5):
        board.append(input[i:i+5])

    result = set()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def dfs(r, c, path):
        if len(path) == 6:
            result.add(path)
            return

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                dfs(nr, nc, path + board[nr][nc])

    for r in range(5):
        for c in range(5):
            dfs(r, c, board[r][c])

    print(len(result))

if __name__ == "__main__":
    solve()
