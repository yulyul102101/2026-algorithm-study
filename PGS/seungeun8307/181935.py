def solution(n):
    if n%2!=0: return sum(i for i in range(1, n+1, 2))

    answer = 0
    no = [i for i in range(0, n+1, 2)]
    for i in no:
        answer+= i**2
        
    return answer