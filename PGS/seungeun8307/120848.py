import math

def solution(n):
    i = 2
    while math.factorial(i) <=n:
        i+=1
    return i-1