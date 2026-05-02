def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        if int(i ** 0.5) ** 2 == i:  # 완전제곱수 체크
            answer -= i
        else:
            answer += i
            
    return answer