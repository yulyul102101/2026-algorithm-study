import math

def solution(numer1, denom1, numer2, denom2):
    l = (denom1*denom2) // math.gcd(denom1,denom2)
    
    numer1 *= l//denom1
    numer2 *= l//denom2
    
    num = numer1+numer2
    
    g = math.gcd(num, l)
    return [num//g, l//g]