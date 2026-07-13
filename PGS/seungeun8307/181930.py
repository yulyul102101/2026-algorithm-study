def solution(a, b, c):
    if a!=b and b!=c and a!=c: 
        answer = a+b+c
    if (a==b and a!=c) or (a==c and a!=b) or (c==b and c!=a): 
        answer = (a+b+c)*(a**2+b**2+c**2)
    if a==b==c:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    return answer