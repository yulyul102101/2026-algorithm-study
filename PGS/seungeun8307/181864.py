def solution(myString, pat):
    s = ''.join(['B' if i=='A' else 'A' for i in myString])
    return 1 if pat in s else 0