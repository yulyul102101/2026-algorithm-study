def solution(price, money, count):
    pc = price*(count*(count+1)/2)
    answer = pc-money
    return answer if answer>0 else 0