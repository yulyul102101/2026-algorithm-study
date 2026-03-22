import sys

N = int(sys.stdin.readline())
o = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

st = 0
for i in range(6):
    if o[i]%T: st+= o[i]//T+1
    else: st+= o[i]//T

print(st)
print(N//P, N%P)