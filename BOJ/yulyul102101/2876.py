import sys

input = sys.stdin.readline

n = int(input())
desks = [tuple(map(int, input().split())) for _ in range(n)]

best_count = 0
best_grade = 1

for grade in range(1, 6):
    current = 0
    max_len = 0

    for a, b in desks:
        if a == grade or b == grade:
            current += 1
            max_len = max(max_len, current)
        else:
            current = 0

    if max_len > best_count:
        best_count = max_len
        best_grade = grade

print(best_count, best_grade)
