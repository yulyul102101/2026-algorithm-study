import sys

input = sys.stdin.readline

n = int(input())
d = 0
p = 0

for _ in range(n):
    win = input().strip()
    if win == "D":
        d += 1
    else:
        p += 1
    if abs(d-p) == 2:
        break

print(f"{d}:{p}")
