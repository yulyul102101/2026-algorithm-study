N = int(input())
X = list(map(int, input().split()))

pos = 0
cnt = 0

for x in X:
    while pos < x - 1:
        if pos + 2 <= x - 1:
            pos += 2
        else:
            pos += 1
        cnt += 1

    if pos != x - 1:
        print(-1)
        exit()

    pos += 2
    cnt += 1

print(cnt)