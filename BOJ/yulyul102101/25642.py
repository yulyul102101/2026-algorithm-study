import sys

a, b = map(int, sys.stdin.readline().split())

while True:
    b += a
    if (b >= 5):
        print("yt")
        break
    a += b
    if (a >= 5):
        print("yj")
        break
