import sys

fbz = []
for i in range(3):
    fbz.append(sys.stdin.readline().strip())

last = fbz[-1]
if last.isdigit():
    nextI = int(last)+1
else:
    for idx, i in enumerate(fbz):
        if i.isdigit(): nextI = int(i) + (3 - idx)

if not nextI % 15: print('FizzBuzz')
elif not nextI % 3: print('Fizz')
elif not nextI % 5: print('Buzz')
else: print(nextI)