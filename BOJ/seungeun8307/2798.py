import sys
import itertools

def closest_sum(L, M):
    result = 0

    for combo in itertools.combinations(L, 3):
        s = sum(combo)
        if s <= M and s > result:
            result = s
    
    return result

N, M= map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
print(closest_sum(L,M))
