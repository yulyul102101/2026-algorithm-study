import sys
import math

n = int(sys.stdin.readline())
rings = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    g = math.gcd(rings[0], rings[i])
    print(f"{rings[0] // g}/{rings[i] // g}")
