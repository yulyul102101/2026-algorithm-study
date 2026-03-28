import sys

A, B, V = map(int, sys.stdin.readline().strip().split())

print((V-A + (A-B)-1 )// (A-B)+1)