import sys

N = int(sys.stdin.readline())

a = [2]
for i in range(N):
    a.append(a[i]*2-1)

print(a[N]**2)