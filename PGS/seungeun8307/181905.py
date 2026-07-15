def solution(my_string, s, e):
    ls = list(my_string)
    ls[s:e+1] = ls[s:e+1][::-1]
    return ''.join(ls)