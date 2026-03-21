import sys

isbn = list(sys.stdin.readline().strip())

idx = 0
total = 0

for i in range(13):
    if isbn[i] == '*':
        idx = i
        continue
    if i % 2 == 0:
        total += int(isbn[i])
    else:
        total += 3 * int(isbn[i])

for k in range(10):
    if idx % 2 == 0:
        if (total + k) % 10 == 0:
            print(k)
            break
    else:
        if (total + 3 * k) % 10 == 0:
            print(k)
            break