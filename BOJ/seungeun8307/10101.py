import sys

a1 = int(sys.stdin.readline())
a2 = int(sys.stdin.readline())
a3 = int(sys.stdin.readline())

if(a1+a2+a3 != 180): print('Error')
elif(a1 == a2 == a3 == 60): print('Equilateral')
elif(a1 == a2 or a1 == a3 or a2 == a3): print('Isosceles')
else: print('Scalene')