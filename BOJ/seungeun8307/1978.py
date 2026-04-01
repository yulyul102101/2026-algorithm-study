import sys

N = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().strip().split()))
a = []

for i in L:
    r = []
    for j in range(1,i+1):
        if(i%j==0): r.append(j)
    if(len(r)==2): a.append(i)

print(len(a))