import sys

n = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(n)]
m = int(sys.stdin.readline().strip())
words2 = [sys.stdin.readline().strip() for _ in range(m)]

idx = words.index('?')

flag_front = True
flag_back = True

if idx == 0:
    flag_front = False

if idx == n-1:
    flag_back = False

front = words[idx-1][-1] if flag_front else ''
back = words[idx+1][0] if flag_back else ''
for word in words2:
    if(word.startswith(front) and word.endswith(back) and word not in words):
        print(word)
        break
