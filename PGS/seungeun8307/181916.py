from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    cnt = Counter(dice)

    if len(cnt) == 1:
        p = dice[0]
        return 1111*p

    if 3 in cnt.values():
        p = [x for x, v in cnt.items() if v == 3][0]
        q = [x for x, v in cnt.items() if v == 1][0]
        return (10*p+q) ** 2

    if sorted(cnt.values()) == [2, 2]:
        p, q = cnt.keys()
        return (p + q) * abs(p - q)

    if 2 in cnt.values():
        p = [x for x, v in cnt.items() if v == 2][0]
        q, r = [x for x, v in cnt.items() if v == 1]
        return q*r

    return min(dice)