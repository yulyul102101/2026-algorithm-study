import sys

n = int(sys.stdin.readline().strip())
marble = [int(x) for x in sys.stdin.readline().split()]

print(2 * (max(marble) - min(marble)))
