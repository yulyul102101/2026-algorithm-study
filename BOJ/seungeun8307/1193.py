import sys

X = int(sys.stdin.readline())
line = 1

while X > line: #대각선 길이 하나씩 늘려가면서 대각선 몇개인지 세기
    X -= line
    line += 1

#a가 분자 b가 분모
if line%2 == 0: a=X ; b=line-X+1
else: a=line-X+1 ; b=X

print(f'{a}/{b}')