import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
else:
    x = 2
    y = 7
    
    i = 1
    while(True):
        if n >= x and n <= y:
            print(i + 1)
            break
        x = x + (i * 6)
        y = y + ((i + 1) * 6)
        i += 1