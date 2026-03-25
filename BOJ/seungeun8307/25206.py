import sys

sc = 0
score = 0
for i in range(20):
    data = sys.stdin.readline().strip().split()
    credit = float(data[1])
    grade = data[2]
    if grade != 'P': 
        sc += credit
        if grade == 'A+': score += credit*4.5 
        elif grade == 'A0': score += credit*4.0
        elif grade == 'B+': score += credit*3.5
        elif grade == 'B0': score += credit*3.0
        elif grade == 'C+': score += credit*2.5
        elif grade == 'C0': score += credit*2.0
        elif grade == 'D+': score += credit*1.5
        elif grade == 'D0': score += credit*1.0
    
print(score/sc)