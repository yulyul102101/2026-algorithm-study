def solution(age):
    m = 'abcdefghij'
    return ''.join(m[int(digit)] for digit in str(age))