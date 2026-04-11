import sys

input = sys.stdin.readline

N, M = map(int, input().split())
K = list(map(int, input().split()))

nums = set()

for k in K:
    for i in range(k, N+1, k):
        nums.add(i)

print(sum(nums))