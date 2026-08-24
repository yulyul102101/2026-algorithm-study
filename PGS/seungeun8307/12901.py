def solution(a, b):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    w = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    days = sum(day[:a-1])+b
    
    return w[(days-1)%7]