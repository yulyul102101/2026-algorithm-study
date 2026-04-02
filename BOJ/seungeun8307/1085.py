import sys

x, y, w, h = map(int,sys.stdin.readline().strip().split())

move = [x, y, h-y, w-x]

print(min(move))