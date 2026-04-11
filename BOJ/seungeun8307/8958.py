import sys

N = int(sys.stdin.readline())

for i in range(N):
    line = sys.stdin.readline().strip()
    score = 0
    c = 0
    for i in line:
        if i == 'O':
            c += 1
            score += c
        else:
            c = 0
    print(score)

