import sys

chs = [sys.stdin.readline().rstrip() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(chs[j]):
            print(chs[j][i], end='')