from collections import Counter

def solution(my_string):
    answer = []
    c = Counter(my_string)
    for i in range(ord('A'), ord('Z')+1):
        answer.append(c.get(chr(i), 0))
        
    for i in range(ord('a'), ord('z')+1):
        answer.append(c.get(chr(i), 0))
        
    return answer