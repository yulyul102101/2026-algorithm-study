import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

D = a*e - b*d
x = (c*e - b*f) // D
y = (a*f - c*d) // D

print(x, y)