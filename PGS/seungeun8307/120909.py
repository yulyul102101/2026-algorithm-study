def solution(n):
    answer = 2
    for i in range(1,n//2):
        if n==i*i: answer=1
    return answer