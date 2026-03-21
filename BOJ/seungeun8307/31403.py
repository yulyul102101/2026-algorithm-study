import sys

A = sys.stdin.readline()
B = sys.stdin.readline()
C = sys.stdin.readline()
print(int(A)+int(B)-int(C))
s = A+B
s = s.replace('\n','')
print(int(s)-int(C))