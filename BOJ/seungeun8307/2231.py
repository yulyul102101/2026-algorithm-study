import sys

N = int(sys.stdin.readline().strip())
R = 0

for i in range(1, N+1):
    num = sum(map(int,str(i)))
    s = i+num

    if s == N: print(i); break
    if i == N: print(0)