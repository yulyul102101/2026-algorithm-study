import itertools

def solution(number):
    answer = 0
    
    for l in itertools.combinations(number, 3):
        if sum(l) == 0:
            answer += 1
            
    return answer