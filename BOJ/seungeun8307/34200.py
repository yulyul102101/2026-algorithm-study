import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

loc = 0
move = 0
s = 0

while(True):
    if s>=N: break

    if loc+1==X[s] and s+1<N and loc+2 == X[s+1]:
        move = -1
        break

    if loc+1==X[s]:
        loc+=2
        move+=1
        s+=1
    elif loc+2==X[s]:
        loc+=1
        move+=1 
    else: 
        loc+=2
        move+=1
    
print(move)