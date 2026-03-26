import sys

targetx, targety = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x == targetx or y == targety:
        print(0)
    else:
        print(1)

