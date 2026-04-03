import sys

N = int(sys.stdin.readline())

x = []
y = []

for i in range(N):
    a ,b = map(int, sys.stdin.readline().split())
    x.append(a)
    y.append(b)

w, h = max(x)-min(x), max(y)-min(y)
print(w*h)