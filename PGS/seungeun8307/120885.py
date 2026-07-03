def solution(bin1, bin2):
    n1, n2 = int(bin1, 2), int(bin2, 2)
    answer = bin(n1 + n2)[2:]
    return answer