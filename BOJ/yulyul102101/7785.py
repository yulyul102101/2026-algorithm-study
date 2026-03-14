import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        s.add(name)
    else:
        s.remove(name)

for name in sorted(s, reverse=True):
    print(name)