import sys

def count_same_chars(a, b):
    return sum(c1 ==c2 for c1, c2 in zip(a, b))

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

res = 0
for i in range(n - 4):
    res = max(res, count_same_chars(s[i:i+5], "eagle"))

print(5 - res)
