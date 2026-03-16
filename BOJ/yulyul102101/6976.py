import sys

n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

for i, num in enumerate(nums):
    b = num

    print(num)

    while abs(b) >= 100:
        a = (b // 10) - (b % 10)
        print(a)
        b = a

    if b % 11 == 0:
        print(f"The number {num} is divisible by 11.")
    else:
        print(f"The number {num} is not divisible by 11.")

    if i != n-1:
        print()
