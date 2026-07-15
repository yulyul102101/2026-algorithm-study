def solution(my_string, n):
    ans = list(my_string)
    return ''.join(ans[-n:])