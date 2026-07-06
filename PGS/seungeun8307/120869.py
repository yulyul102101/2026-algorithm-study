def solution(spell, dic):
    answer = 2
    for i in dic:
        if all(s in i for s in spell): answer=1
    return answer