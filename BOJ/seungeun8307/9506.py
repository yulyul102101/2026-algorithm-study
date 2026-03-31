import sys

while(True):
    a = []
    n = int(sys.stdin.readline())
    if(n==-1): break
    for i in range(1,n):
        if(n%i==0): a.append(i)
    if(sum(a)==n): 
        print(n,'=',end=' ')
        print(*a,sep=' + ')
    else: print(n,'is NOT perfect')