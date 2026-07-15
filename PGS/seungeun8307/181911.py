def solution(my_strings, parts):
    answer = ''
    for (s, e), part in zip(parts, my_strings):
        answer += part[s:e+1]
            
    return answer