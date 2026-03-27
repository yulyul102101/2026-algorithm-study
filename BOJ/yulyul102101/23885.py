import sys

n, m = map(int, sys.stdin.readline().split())
sx, sy = map(int, sys.stdin.readline().split())
ex, ey = map(int, sys.stdin.readline().split())

if sx == ex and sy == ey:
    print("YES")
elif n == 1 or m == 1:
    print("NO")
elif (sx + sy) % 2 == (ex + ey) % 2:
    print("YES")
else:
    print("NO")
