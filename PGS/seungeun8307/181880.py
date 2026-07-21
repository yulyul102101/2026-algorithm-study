def solution(num_list):
    answer = 0
    for i in num_list:
        answer += i.bit_length()-1
    return answer