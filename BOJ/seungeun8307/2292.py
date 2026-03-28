import sys

N = int(sys.stdin.readline().strip())

level = 1
c = 1

while N>level:
    level += 6*c
    c += 1

print(c)