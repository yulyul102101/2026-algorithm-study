import sys

numbers = []
for _ in range(5):
    numbers.append(int(sys.stdin.readline()))

print(sum(numbers) // 5)

numbers.sort()
print(numbers[2])