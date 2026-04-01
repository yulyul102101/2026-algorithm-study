import sys
import math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

prime = []
for i in range(N, M+1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)

if prime: print(sum(prime));print(min(prime))
else: print(-1)