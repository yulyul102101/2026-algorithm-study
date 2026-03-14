import sys

n = int(sys.stdin.readline())

log = {}
for i in range(n):
    e, w = sys.stdin.readline().split()
    log[e] = w

find = "enter"
inC = list(filter(lambda k: log[k] == find, log))

print('\n'.join(inC))
