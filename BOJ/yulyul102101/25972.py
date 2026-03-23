import sys

n = int(sys.stdin.readline())
dominos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dominos.sort(key=lambda x: x[0])

ans = 1

for i in range(n - 1):
    if dominos[i][0] + dominos[i][1] < dominos[i + 1][0]:
        ans += 1

print(ans)
