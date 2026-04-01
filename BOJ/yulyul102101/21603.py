import sys

input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
k = k % 10

for i in range(1, n+1):
    if str(i).endswith(str(k)) or str(i).endswith(str((2 * k) % 10)):
        continue
    arr.append(i)

print(len(arr))
print(*arr)
