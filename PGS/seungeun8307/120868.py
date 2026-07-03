def solution(sides):
    l = [i for i in range(abs(sides[0]-sides[1])+1, sum(sides))]
    answer = len(l)
    
    return answer