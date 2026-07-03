from math import factorial as ft

def solution(balls, share):
    answer = ft(balls) / (ft(balls-share)*ft(share))
    return answer