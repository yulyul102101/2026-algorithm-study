def solution(a, b):
    if a%2!=0 and b%2!=0: answer = a**2 + b**2
    elif a%2==0 and b%2==0: answer = abs(a-b)
    else: answer = (a+b)*2
    return answer