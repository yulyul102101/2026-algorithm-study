import sys

while(True):
    T = list(map(int, sys.stdin.readline().split()))
    if T[0]==T[1]==T[2]==0: break
    if sum(T)-max(T) <= max(T): print('Invalid')
    elif T[0]==T[1]==T[2]: print('Equilateral')
    elif T[0]!=T[1] and T[0]!=T[2] and T[1]!=T[2]: print('Scalene')
    else: print('Isosceles')