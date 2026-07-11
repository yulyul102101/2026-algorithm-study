def solution(a, b):
    ab = int(str(a)+str(b))
    ab2 = a*b*2
    return max(ab2, ab)