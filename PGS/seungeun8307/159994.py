def solution(cards1, cards2, goal):
    a, b = 0, 0
    for word in goal:
        if a<len(cards1) and cards1[a] == word:
            a += 1
        elif b<len(cards2) and cards2[b] == word:
            b+= 1
        else: return "No"
    return "Yes"