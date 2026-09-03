from itertools import combinations

def prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for c in combinations(nums, 3):
        if prime(sum(c)):
            answer += 1
    
    return answer