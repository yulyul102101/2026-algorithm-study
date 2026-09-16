def solution(n):
    dig = ''
    while n>0:
        dig += str(n%3)
        n//=3
        
    return int(dig, 3)