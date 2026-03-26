import sys

paper = [[0 for _ in range(100)]for _ in range(100)]

N = int(sys.stdin.readline())

for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1

print(sum(sum(row)for row in paper))