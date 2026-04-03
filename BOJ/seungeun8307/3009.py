import sys


x1,y1 = map(int, sys.stdin.readline().split())
x2,y2 = map(int, sys.stdin.readline().split())
x3,y3 = map(int, sys.stdin.readline().split())

xa = [x1,x2,x3]
ya = [y1,y2,y3]

for i in xa:
    if xa.count(i) == 1: x4 = i
for j in ya:
    if ya.count(j) == 1: y4 = j

print(x4,y4)