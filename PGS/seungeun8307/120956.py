import re

def solution(babbling):
    answer = 0
    baby = ['aya','ye','woo','ma']
    
    for word in babbling:
        pattern = re.compile('^(aya|ye|woo|ma)+$')
        if pattern.match(word):
            answer += 1
    
    return answer