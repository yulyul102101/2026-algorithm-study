import sys

lines = [line.strip() for line in sys.stdin]

for line in lines:
    x = 1
    y = int(line)

    while x % y != 0:
        x *= 10
        x += 1

    print(len(str(x)))
