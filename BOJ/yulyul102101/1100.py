import sys

chess = [sys.stdin.readline().strip() for _ in range(8)]

res = 0

for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0 and chess[i][j] == 'F':
                res += 1
    else:
        for j in range(8):
            if j % 2 != 0 and chess[i][j] == 'F':
                res += 1

print(res)