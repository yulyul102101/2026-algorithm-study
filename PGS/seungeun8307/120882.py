import statistics

def solution(score):
    answer = []
    avg = [statistics.mean(i) for i in score]
        
    for x in avg:
        rank = sum(y > x for y in avg) + 1
        answer.append(rank)
        
    return answer