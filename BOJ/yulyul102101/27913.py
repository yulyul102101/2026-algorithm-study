import sys

n, q = map(int, sys.stdin.readline().split())

n = list(("SciComLove" * 200000)[:n])
cnt = sum(c.isupper() for c in n)

for _ in range(q):
    x = int(sys.stdin.readline().strip())
    if n[x - 1].isupper():
        n[x - 1] = n[x - 1].lower()
        cnt -= 1
    elif n[x - 1].islower():
        n[x - 1] = n[x - 1].upper()
        cnt += 1
    print(cnt)
